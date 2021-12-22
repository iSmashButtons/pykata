# **Find Cost of Tile to Cover W x H Floor** - Calculate the total cost of tile
# it would take to cover a floor plan of width and height, using a cost entered
# by the user.

# I'm assuming each tile is 1 square foot in size.

WIDTH = 30
HEIGHT = 40

def calculate_total_cost(tprice):
    area = (WIDTH * HEIGHT)
    total_cost = (area * tprice)
    return total_cost

while True:
    print('Enter the price of each tile (q to quit)')
    try:
        tile_price = input('>>> ')
        if 'q' in tile_price:
            break
        tile_price = float(tile_price)
        print(f'Total cost of floor: {calculate_total_cost(tile_price)}')
    except:
        print('Numbers only please!')