from fastapi import APIRouter

router = APIRouter(
    tags=['Stripe'],
    prefix= '/stripe'
)

YOUR_DOMAIN = 'http://localhost'

@router.post('/checkout')
async def stripe_checkout():
    try:
        checkout_session = stripe_checkout.Session.create(
            line_items=[
                {
                    #PriceId du produit 

                    'price': 'price_1O51yVK0YwCh5FYNcyv9C8Zd',
                    'quantity': 1,
                },
            ],
            mode= 'payement',
            payment_method_types=['card'],
            succes_url= YOUR_DOMAIN + '/succes.html',
            cancel_url= YOUR_DOMAIN + '/cancel.html',

        )
        return checkout_session
    except Exception as e:
        return str(e)
    

