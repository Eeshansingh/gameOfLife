import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animations
import argparse

import json

with open('C:/Users/Eeshan Singh/Desktop/db.json') as f:
        data = json.load(f)
players=dict(data)

def algo(x, y, universe):
    neighbours = np.sum(universe[x - 1 : x + 2, y - 1 : y + 2]) - universe[x, y]
    
    if universe[x, y] and not 2 <= neighbours <= 3:
        return 0
    elif neighbours == 3:
        return 1
    return universe[x, y]

def animation(universe_size,seed,n_generations=30,interval=200):
    
    # Initialise the universe and seed
    universe = np.zeros(universe_size)
    x_start, y_start = 40, 15
    seed_array = np.array(players[seed])
    
    x_end, y_end = x_start + seed_array.shape[0], y_start + seed_array.shape[1]
    universe[x_start:x_end, y_start:y_end] = seed_array

    # Animate
    fig = plt.figure()
    plt.axis("off")
    ims = []
    print(n_generations)
    for i in range(n_generations):
        ims.append((plt.imshow(universe),))
        new_universe = np.copy(universe)
        for i in range(universe.shape[0]):
            for j in range(universe.shape[1]):
                new_universe[i, j] = algo(i, j, universe)
        universe = new_universe
    
    im_ani = animations.ArtistAnimation(
        fig, ims, interval=interval, repeat_delay=2000, blit=True
    )
    im_ani.save((str(seed) + ".htm"))


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--universe-size",
        type=str,
        default="50,50")
    parser.add_argument(
        "-seed", type=str, default="Bellerin")
    parser.add_argument(
        "-n", type=int, default=30, help="number of universe iterations")
    parser.add_argument(
        "-interval",
        type=int,
        default=200)

    args = parser.parse_args()

    animation(
        universe_size=(
            int(args.universe_size.split(",")[0]),
            int(args.universe_size.split(",")[1]),
        ),
        seed=args.seed,   
        n_generations=args.n,
        interval=args.interval,
        
    )