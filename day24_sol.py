class Attack:

    def __init__(self, _name, _damage, _initiative):
        self.name = _name
        self.damage = _damage
        self.initiative = _initiative

    def __str__(self):
        attrs = {
            'name': self.name,
            'damage': self.damage,
            'initiative': self.initiative
        }
        return "{damage} {name} damage at initiative {initiative}".format(**attrs)


class Group:

    def __init__(self, _num_units, _hp, _weaknesses, _immunities, _attack, _team, _id):
        self.num_units = _num_units
        self.hp = _hp
        self.weaknesses = _weaknesses
        self.immunities = _immunities
        self.attack = _attack
        self.team = _team
        self.id = _id

    def effective_power(self):
        return self.num_units * self.attack.damage

    def dead(self):
        return self.effective_power() <= 0

    def select_target(self, other_groups):
        max_damage, targets = 1, []
        for group in other_groups:
            dam = self.attack_damage(group)
            if dam > 0:
                targets.append(group)
                print(
                    "{0} group {1} would deal defending group {2} {3} damage".format(
                        self.team, self.id, group.id, dam))
        targets.sort(key=lambda g: (g.effective_power(), g.attack.initiative))

        return targets

    def fight(self, other):
        damage = self.attack_damage(other)
        killed = min(damage // other.hp, other.num_units)
        print("{0} group {1} attacks defending group {2}, killing {3} units".format(
            self.team, self.id, other.id, killed)
        )
        other.num_units -= killed

    def attack_damage(self, other):
        if self.attack.name in other.immunities:
            return 0
        return self.effective_power() * (1 + 1 * (self.attack.name in other.weaknesses))

    def __str__(self):
        special = {}
        if self.immunities:
            special['immune'] = "immune to " + ', '.join(self.immunities)
        if self.weaknesses:
            special['weakness'] = "weak to " + ', '.join(self.weaknesses)
        inner = '(' + '; '.join(special.values()) + ')'
        attrs = {
            'special': inner,
            'units': self.num_units,
            'hp': self.hp,
            'attack': str(self.attack),
        }
        res = "{units} units each with {hp} hit points {special} with an attack that does {attack}"
        return res.format(**attrs)


class Army:
    def __init__(self, _name):
        self.name = _name
        self.groups = []

    def add_group(self, group):
        assert (isinstance(group, Group))
        self.groups.append(group)

    def alive(self):
        return not all(g.dead() for g in self.groups)

    def __str__(self):
        if any(not g.dead() for g in self.groups):
            return self.name + ":\n" + '\n'.join(
                "Group {0} contains {1} units".format(i + 1, group.num_units)
                for i, group in enumerate(self.groups) if group.num_units > 0
            )
        else:
            return self.name + ":\n" + "No groups remain."


def parse(sentence):
    words = line.split()
    res = {
        'units': int(words[0]),
        'hp': int(words[4]),
        'initiative': int(words[-1]),
        'name': words[-5],
        'damage': int(words[-6])
    }
    rest = {'immune': [], 'weak': []}
    if '(' in sentence:
        inner = line[line.index('(') + 1:line.index(')')]
        inner = inner.replace(',', '')
        inner = inner.split('; ')
        rest[inner[0].split()[0]] += inner[0].split()[2:]
        if len(inner) == 2:
            rest[inner[1].split()[0]] += inner[1].split()[2:]
    res.update(rest)
    return res


def print_armies():
    for a in armies:
        print(armies[a])
    print('')


if __name__ == '__main__':
    with open('data/day24test') as data:
        lines = data.readlines()
        armies = {
            'Immune System': Army('Immune System'),
            'Infection': Army('Infection')
        }
        group_name = ''
        for line in lines:
            line = line.strip()
            if ':' in line:
                group_name = line[:-1]
            elif not line:
                pass
            else:
                line_dict = parse(line)
                new_attack = Attack(
                    _name=line_dict['name'],
                    _damage=line_dict['damage'],
                    _initiative=line_dict['initiative']
                )
                new_group = Group(
                    _num_units=line_dict['units'],
                    _hp=line_dict['hp'],
                    _immunities=line_dict['immune'],
                    _weaknesses=line_dict['weak'],
                    _attack=new_attack,
                    _team=group_name,
                    _id=len(armies[group_name].groups) + 1
                )
                if not (str(new_group) == line):
                    print(new_group)
                    print(line)
                # assert (str(new_group) == line)
                armies[group_name].add_group(new_group)

        rnd = 1
        while all(army.alive() for army in armies.values()):
            print("Round number %d ---------------------- fight" % rnd)
            print_armies()
            all_groups = armies['Infection'].groups + armies['Immune System'].groups
            alive_groups = [g for g in all_groups if not g.dead()]

            # Phase: select targets
            target_map = {}
            for g in alive_groups:
                t = g.select_target([
                    og for og in alive_groups
                    if og.team != g.team and og not in target_map.values()
                ])
                if t:
                    target_map[g] = t[-1]
            print()

            alive_groups.sort(key=lambda g: g.attack.initiative)
            alive_groups.reverse()

            # Phase: attack selected targets
            for g in alive_groups:
                if g.num_units > 0 and g in target_map:
                    g.fight(target_map[g])
            print()
            rnd += 1

        print_armies()

        all_groups = armies['Infection'].groups + armies['Immune System'].groups
        alive_groups = [g for g in all_groups if not g.dead()]
        print(sum(g.num_units for g in alive_groups))
