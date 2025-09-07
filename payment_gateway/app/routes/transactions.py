from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database         # ✅ absolute imports


# 👇 this must come before any @router usage
router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.post("/")
def create_transaction(transaction: schemas.TransactionCreate, db: Session = Depends(database.SessionLocal)):
    customer = db.query(models.User).filter(models.User.role == models.Role.customer).first()  # placeholder
    merchant = db.query(models.User).filter(models.User.id == transaction.merchant_id).first()

    if not merchant or merchant.role != models.Role.merchant:
        raise HTTPException(status_code=400, detail="Invalid merchant")

    if customer.balance < transaction.amount:
        status = models.TransactionStatus.failed
    else:
        customer.balance -= transaction.amount
        merchant.balance += transaction.amount
        status = models.TransactionStatus.success

    db_txn = models.Transaction(
        customer_id=customer.id,
        merchant_id=merchant.id,
        amount=transaction.amount,
        status=status,
    )
    db.add(db_txn)
    db.commit()
    db.refresh(db_txn)

    return {"transaction_id": db_txn.id, "status": db_txn.status.value}

