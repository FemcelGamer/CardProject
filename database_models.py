import enum

from sqlalchemy import String, Boolean, Integer, Enum, JSON
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


class Base(DeclarativeBase):
	pass

class DamageType(enum.Enum):
	necrotic = 'necrotic'
	radiant = 'radiant'
	force = 'force'
	fire = 'fire'
	cold = 'cold'
	thunder = 'thunder'
	lightning = 'lightning'
	acid = 'acid'
	poison = 'poison'
	slashing = 'slashing'
	piercing = 'piercing'
	psychic = 'psychic'
	bludgeoning = 'bludgeoning'

class SchoolType(enum.Enum):
	abjuration = 'abjuration'
	conjuration = 'conjuration'
	divination = 'divination'
	enchantment = 'enchantment'
	evocation = 'evocation'
	illusion = 'illusion'
	necromancy = 'necromancy'
	transmutation = 'transmutation'
#
class SpellLevelType(enum.Enum):
	cantrip = 'cantrip'
	first = '1 level'
	second = '2 level'
	third = '3 level'
	fourth = '4 level'
	fifth = '5 level'
	sixth = '6 level'
	seventh = '7 level'
	eighth = '8 level'
	ninth = '9 level'
#
class DurationType(enum.Enum):
	instantaneous = 'instantaneous'
	oneMinute = '1 minute'
	tenMinutes = '10 minutes'
	oneHour = '1 hour'
	eightHours = '8 hours'
	day = '24 hours'

class CastingTimeType(enum.Enum):
	action_cast = 'action'
	bonus_cast = 'bonus action'
	reaction_cast = 'reaction'
	other_cast = 'period of time'
#
class ConditionType(enum.Enum):
	Blinded = 'Blinded'
	Charmed = 'Charmed'
	Deafened = 'Deafened'
	Exhaustion = 'Exhaustion'
	Frightened = 'Frightened'
	Grappled = 'Grappled'
	Incapacitated = 'Incapacitated'
	Invisible = 'Invisible'
	Paralyzed = 'Paralyzed'
	Petrified = 'Petrified'
	Poisoned = 'Poisoned'
	Prone = 'Prone'
	Restrained = 'Restrained'
	Stunned = 'Stunned'
	Unconscious = 'Unconscious'
	Bloodied = 'Bloodied'

class SavingThrowType(enum.Enum):
	strength = 'STR'
	dexterity = 'DEX'
	constitution = 'CON'
	wisdom = 'WIS'
	intelligence = 'INT'
	charisma = 'CHA'
#
class HitType(enum.Enum):
	on_hit = 'to hit'
	saving_throw = 'saving throw'

class ComponentsType(enum.Enum):
	somatic = 'S'
	verbal = 'V'
	material = 'M'

class Card(Base):
    # исправлены типы Enum, Boolean
    tablename = 'cards'
    card_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    damage_type: Mapped[DamageType] = mapped_column(Enum(DamageType))
    average_damage: Mapped[int] = mapped_column(Integer)
    effect: Mapped[str] = mapped_column(String)
    attack_type: Mapped[bool] = mapped_column(Boolean)
    concentration: Mapped[bool] = mapped_column(Boolean)
    duration_type: Mapped[DurationType] = mapped_column(Enum(DurationType))
    school_type: Mapped[SchoolType] = mapped_column(Enum(SchoolType))
    level_type: Mapped[SpellLevelType] = mapped_column(Enum(SpellLevelType))
    casting_time_type: Mapped[CastingTimeType] = mapped_column(Enum(CastingTimeType))
    reaction_trigger: Mapped[str] = mapped_column(String)
    condition_type: Mapped[ConditionType] = mapped_column(Enum(ConditionType))
    condition: Mapped[bool] = mapped_column(Boolean)
    spell_slot_upcast: Mapped[str] = mapped_column(String)
    range: Mapped[int] = mapped_column(Integer)
    radius: Mapped[int] = mapped_column(Integer)
    saving_throw_type: Mapped[SavingThrowType] = mapped_column(Enum(SavingThrowType))
    hit_type: Mapped[HitType] = mapped_column(Enum(HitType))
    damage: Mapped[bool] = mapped_column(Boolean)
    components: Mapped[list[str]] = mapped_column(JSON, default=list)
	# damage_XdY: '??'
	# components: rethink as multi-value (string/flags/table) rather than single enum



# import random

# def roll_dice(num_dice, sides):
#     rolls = []
#     total = 0
#     for _ in range(num_dice):
#         # Generate random number between 1 and the sides (e.g., 1-20)
#         roll = random.randint(1, sides)
#         rolls.append(roll)
#         total += roll
#     return total, rolls

# # Example: Roll 3d6 (3 dice, 6 sides)
# num_dice = 3
# sides = 6
# total, individual_rolls = roll_dice(num_dice, sides)

# print(f"Rolling {num_dice}d{sides}:")
# print(f"Individual Rolls: {individual_rolls}")
# print(f"Total: {total}")


# Функционал книги заклинаний:
# сохранение в свою книгу заклинаний и удаление, 
# фильтр по заклинаниям, поиск, 
# создание новых заклинаний и удаление (отдельный лист с хоумбрю)








