from fastapi import FastAPI, HTTPException, status

app = FastAPI()

orders_list = [
    {"id": 1, "code": "SP001", "payment_status": "PAID", "method": "BANK_TRANSFER"},
    {"id": 2, "code": "SP002", "payment_status": "UNPAID", "method": "NONE"}
]

orders_dict = {order["id"]: order for order in orders_list}

@app.get("/orders/{order_id}/payment")
def get_order_payment(order_id: int):
    try:
        order = orders_dict.get(order_id)
        
        if order is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Order not found"
            )
            
        return {
            "order_id": order["id"],
            "payment_status": order["payment_status"],
            "method": order["method"]
        }
        
    except HTTPException as http:
        raise http
        
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )