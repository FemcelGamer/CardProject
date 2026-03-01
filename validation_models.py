
from typing import Annotated

from pydantic import BaseModel, Field

from database_models import DamageType, ConditionType, SavingThrowType, HitType, SpellLevelType, DurationType, \
    SchoolType, CastingTimeType

TitleType = Annotated[str, Field(min_length=5, max_length=100)]
DescriptionType = Annotated[str, Field(min_length=10, max_length=500)]
AverageDamageType = Annotated[int, Field(ge=0, le=1000)]
EffectType = Annotated[str, Field(min_length=5, max_length=100)]
ReactionType = Annotated[str, Field(min_length=5, max_length=100)]
UpcastType = Annotated[str, Field(min_length=5, max_length=100)]
RangeType = Annotated[int, Field(ge=0, le=1000)]
RadiusType = Annotated[int, Field(ge=0, le=1000)]

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
    components: set[str] = Field(default_factory=set)



    #дописать все тайпы дома: интенжеры и стринги в аннотации,
    #остальные -- наследуют
    #домашка
