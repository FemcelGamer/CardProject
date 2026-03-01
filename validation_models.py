# class Card(Base):
#     # исправлены типы Enum, Boolean
#     tablename = 'cards'
#     card_id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     title: Mapped[str] = mapped_column(String)
#     description: Mapped[str] = mapped_column(String)
#     damage_type: Mapped[DamageType] = mapped_column(Enum(DamageType))
#     spell_level: Mapped[int] = mapped_column(Integer)
#     average_damage: Mapped[int] = mapped_column(Integer)
#     effect: Mapped[str] = mapped_column(String)
#     attack_type: Mapped[bool] = mapped_column(Boolean)
#     concentration: Mapped[bool] = mapped_column(Boolean)
#     duration_type: Mapped[DurationType] = mapped_column(Enum(DurationType))
#     school_type: Mapped[SchoolType] = mapped_column(Enum(SchoolType))
#     level_type: Mapped[SpellLevelType] = mapped_column(Enum(SpellLevelType))
#     casting_time_type: Mapped[CastingTimeType] = mapped_column(Enum(CastingTimeType))
#     reaction_trigger: Mapped[str] = mapped_column(String)
#     condition_type: Mapped[ConditionType] = mapped_column(Enum(ConditionType))
#     condition: Mapped[bool] = mapped_column(Boolean)
#     spell_slot_upcast: Mapped[str] = mapped_column(String)
#     range: Mapped[int] = mapped_column(Integer)
#     radius: Mapped[int] = mapped_column(Integer)
#     saving_throw_type: Mapped[SavingThrowType] = mapped_column(Enum(SavingThrowType))
#     hit_type: Mapped[HitType] = mapped_column(Enum(HitType))
#     damage: Mapped[bool] = mapped_column(Boolean)
#     components: Mapped[list[str]] = mapped_column(JSON, default=list)
from typing import Annotated

from pydantic import BaseModel

from database_models import DamageType

TitleType = Annotated[str, Field(min_length=5, max_length=100)]
DescriptionType = Annotated[str, Field(min_length=10, max_length=500)]
AverageDamageType = Annotated[int, Field(ge=0, le=1000)]
EffectType = Annotated[str, Field(min_length=5, max_length=100)]
ReactionType = Annotated[str, Field(min_length=5, max_length=100)]
UpcastType = Annotated[str, Field(min_length=5, max_length=100)]
RangeType = Annotated[int, Field(ge=0, le=1000)]
RadiusType = Annotated[int, Field(ge=0, le=1000)]
ComponentsType = Annotated[list, Field(ge=0, le=1000)]

class CardBase(BaseModel):
    card_title: TitleType
    description: DescriptionType
    damage_type: DamageType
    average_damage: AverageDamageType
    attack_type: bool
    effect: EffectType
    concentration: bool
    duration_type: DurationType
    school_type: SchoolType
    level_type: SpellLevelType
    casting_time_type: CastingTimeType
    reaction_trigger: ReactionType
    condition_type: ConditionType
    condition: bool
    spell_slot_upcast: UpcastType
    range: RangeType
    radius: RadiusType
    saving_throw_type: SavingThrowType
    hit_type: HitType
    damage: bool
    components: ComponentsType



    #дописать все тайпы дома: интенжеры и стринги в аннотации,
    #остальные -- наследуют
    #домашка
