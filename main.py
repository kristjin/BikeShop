import bike

if __name__ == '__main__':
    
    store = bike.Shop("Intrepid Moustache Rides", 0.20)
    
    B1 = bike.Bicycle("Rickety Racket", 10, 5)
    B2 = bike.Bicycle("Silver Ferret", 100, 1)
    B3 = bike.Bicycle("Star Rider", 250, 10)
    B4 = bike.Bicycle("Slobber Slick", 400, 10)
    B5 = bike.Bicycle("Wicked Trickster", 750, 15)
    B6 = bike.Bicycle("Sausage Maker", 800, 2)
    bikes = {B1, B2, B3, B4, B5, B6}    
    
    C1 = bike.Customer("MC Hammer", 200)
    C2 = bike.Customer("Bill Maher", 500)
    C3 = bike.Customer("Skrillex", 1000)
    customers = {C1, C2, C3}
    
    store.reportStock(bikes)
    
    for c in customers:
        c.greet()
        store.makePitch(c, bikes)
    
    store.reportStock(bikes)
    store.reportProfit()