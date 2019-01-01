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
        self.boost = 0

    def effective_power(self):
        return self.num_units * (self.attack.damage + self.boost)

    def set_boost(self, _boost):
        self.boost = _boost

    def dead(self):
        return self.effective_power() <= 0

    def select_target(self, other_groups):
        targets = []
        for group in other_groups:
            dam = self.attack_damage(group)
            if dam > 0:
                targets.append(group)
                message = "{0} group {1} would deal defending group {2} {3} damage"
                # print(message.format(self.team, self.id, group.id, dam))
        return sorted(
            targets,
            key=lambda g: (self.attack_damage(g), g.effective_power(), g.attack.initiative)
        )

    def fight(self, other):
        damage = self.attack_damage(other)
        killed = min(damage // other.hp, other.num_units)
        message = "{0} group {1} attacks defending group {2}, killing {3} units"
        # print(message.format(self.team, self.id, other.id, killed))
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
        inner = '(' + '; '.join(special.values()) + ') ' if special.values() else ''
        attrs = {
            'special': inner,
            'units': self.num_units,
            'hp': self.hp,
            'attack': str(self.attack),
        }
        res = "{units} units each with {hp} hit points {special}with an attack that does {attack}"
        return res.format(**attrs)


class Army:
    def __init__(self, _name):
        self.name = _name
        self.groups = []

    def set_boost(self, _boost):
        for g in self.groups:
            g.set_boost(_boost)

    def add_group(self, group):
        assert (isinstance(group, Group))
        self.groups.append(group)

    def alive(self):
        return not all(g.dead() for g in self.groups)

    def __str__(self):
        if any(not g.dead() for g in self.groups):
            return self.name + ":\n" + '\n'.join(
                "Group {0} contains {1} units".format(i + 1, group.num_units)
                for i, group in enumerate(self.groups) if group.num_units > 0)
        else:
            return self.name + ":\n" + "No groups remain."


def parse(sentence):
    words = sentence.split()
    res = {
        'units': int(words[0]),
        'hp': int(words[4]),
        'initiative': int(words[-1]),
        'name': words[-5],
        'damage': int(words[-6])
    }
    rest = {'immune': [], 'weak': []}
    if '(' in sentence:
        inner = sentence[sentence.index('(') + 1:sentence.index(')')]
        inner = inner.replace(',', '')
        inner = inner.split('; ')
        rest[inner[0].split()[0]] += inner[0].split()[2:]
        if len(inner) == 2:
            rest[inner[1].split()[0]] += inner[1].split()[2:]
    res.update(rest)
    return res


def load_armies():
    with open('data/day24') as data:
        lines = data.readlines()
        res = {
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
                    _id=len(res[group_name].groups) + 1
                )
                res[group_name].add_group(new_group)
    return res


def part1(armies, boost):
    armies['Immune System'].set_boost(boost)
    all_groups = armies['Infection'].groups + armies['Immune System'].groups
    while all(army.alive() for army in armies.values()):
        # print_dict(armies)
        alive = [g for g in all_groups if not g.dead()]

        # Phase: select targets
        alive.sort(key=lambda g: (g.effective_power(), g.attack.initiative), reverse=True)
        target_map = {}
        for g in alive:
            t = g.select_target([
                og for og in alive
                if og.team != g.team and og not in target_map.values()
            ])
            if t:
                target_map[g] = t[-1]

        # Phase: attack selected targets
        alive.sort(key=lambda g: g.attack.initiative, reverse=True)
        for g in alive:
            if g.num_units > 0 and g in target_map:
                g.fight(target_map[g])

        # print_dict(armies)
    winner = 'Immune System' if armies['Immune System'].alive() else "Infection"
    return winner, sum(g.num_units for g in all_groups if not g.dead())


if __name__ == '__main__':

    print("part 1:", part1(armies=load_armies(), boost=0)[1])

    # Part 2
    b = 188
    # increasing by 1 doesn't work because 187 runs indefinitely
    # Better would be binary search (but this could still fail at 187
    while part1(armies=load_armies(), boost=b)[0] == "Infection":
        b += 1

    print("part 2:", part1(armies=load_armies(), boost=b)[1])
