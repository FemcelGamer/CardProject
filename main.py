from fastapi import FastAPI, HTTPException, Depends

from database import SessionLocal
from database_models import Card
from sqlalchemy.orm import Session

from validation_models import CardOutput, CardCreate, CardUpdate

app = FastAPI()

def get_session():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()

#get all
@app.get('/api/cards', response_model=list[CardOutput])
def get_all_cards(session : Session = Depends(get_session)):
	return session.query(Card).order_by(Card.title).all()

# CREATE
@app.post('/api/cards', response_model=CardCreate)
def add_card(card: Card,
			 session: Session = Depends(get_session)):
	db_card = Card(
		title=card.title,
		description=card.description,
		damage_type=card.damage_type,
		average_damage=card.average_damage,
		effect=card.effect,
		attack_type=card.attack_type,
		concentration=card.concentration,
		duration_type=card.duration_type,
		school_type=card.school_type,
		level_type=card.level_type,
		casting_time_type=card.casting_time_type,
		reaction_trigger=card.reaction_trigger,
		condition_type=card.condition_type,
		condition=card.condition,
		spell_slot_upcast=card.spell_slot_upcast,
		range=card.range,
		radius=card.radius,
		saving_throw_type=card.saving_throw_type,
		hit_type=card.hit_type,
		damage=card.damage,
		components=card.components
	)
	session.add(db_card)
	session.commit()
	session.refresh(db_card)
	return db_card

# GET BY ID
@app.get('/api/cards/{card_id}', response_model=CardOutput)
def get_card_by_id(card_id: int, session: Session = Depends(get_session)):
	db_card = session.query(Card).filter(Card.card_id == card_id).first()

	if not db_card:
		raise HTTPException(status_code=404, detail="Card not found")

	return db_card

@app.delete('/api/cards/{card_id}')
def delete_card(card_id: int, session: Session = Depends(get_session)):
	db_card = session.query(Card).filter(Card.card_id == card_id).first()

	if not db_card:
		raise HTTPException(status_code=404, detail="Card not found")

	session.delete(db_card)
	session.commit()
	session.refresh(db_card)
	return {'Message': f'Card with {card_id} successfully deleted',}


@app.patch('/api/cards/{card_id}', response_model=CardUpdate)
def update_card(card_id: int, session: Session = Depends(get_session)):
	db_card = session.query(Card).filter(Card.card_id == card_id).first()

	if not db_card:
		raise HTTPException(status_code=404, detail="Card not found")

	session.commit()
	session.refresh(db_card)
	return db_card


# if name in items:
	# 	items.remove(name)
	# 	return items
	# raise HTTPException(404, 'Invalid data: item not found, punk')

