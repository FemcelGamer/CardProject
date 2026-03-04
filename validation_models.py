
from typing import Annotated

from pydantic import BaseModel, Field, ConfigDict

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
# card_id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     title: Mapped[str] = mapped_column(String)
#     description: Mapped[str] = mapped_column(String)
#     damage_type: Mapped[DamageType] = mapped_column(Enum(DamageType))
#     average_damage: Mapped[int] = mapped_column(Integer)
#     effect: Mapped[str] = mapped_column(String)
# reaction_trigger: Mapped[str] = mapped_column(String)
#     condition_type: Mapped[ConditionType] = mapped_column(Enum(ConditionType))
#     condition: Mapped[bool] = mapped_column(Boolean)
#     spell_slot_upcast: Mapped[str] = mapped_column(String)
#     range: Mapped[int] = mapped_column(Integer)
#     radius: Mapped[int] = mapped_column(Integer)


class CardBase(BaseModel):
    title: TitleType
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

class CardCreate(BaseModel):
    title: TitleType
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

class CardUpdate(BaseModel):
    card_title: TitleType | None = None
    description: DescriptionType | None = None
    damage_type: DamageType | None = None
    average_damage: AverageDamageType | None = None
    attack_type: bool | None = None
    effect: EffectType | None = None
    concentration: bool | None = None
    duration_type: DurationType | None = None
    school_type: SchoolType | None = None
    level_type: SpellLevelType | None = None
    casting_time_type: CastingTimeType | None = None
    reaction_trigger: ReactionType | None = None
    condition_type: ConditionType | None = None
    condition: bool | None = None
    spell_slot_upcast: UpcastType | None = None
    range: RangeType | None = None
    radius: RadiusType | None = None
    saving_throw_type: SavingThrowType | None = None
    hit_type: HitType | None = None
    damage: bool | None = None
    components: set[str] | None = None

class CardOutput(CardBase):
    model_config = ConfigDict(from_attributes=True)