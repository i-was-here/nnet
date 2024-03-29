from nnet.nn.val.nn import MLP
from nnet.optimizers.optimizers import GD
from nnet.losses.losses import mse_loss
from nnet.visualize.draw_graph import draw_dot
import random
random.seed(42)


if __name__=="__main__":

    # hyper params initialization
    epochs = 20
    lr = 0.01

    # data initialization
    x = [
        [3.0, 4.0, 5.0],
        [-5.0, -2.0, 8.0],
        [-2.0, 2.5, -4.5],
        [2.0, -1.5, -4.0]
    ]
    y_true = [1, -1, -1, 1]
    
    # model initialization
    model = MLP(3, [4, 4, 1])
    optim = GD(model.parameters(), lr)
    # optim_mbgd = MBGD(model.parameters(), lr, gamma=0.9)
    # optim = SGD(model.parameters(), lr, 0.9, nestrov=True)

    # training loop
    for epoch in range(epochs):

        # forward pass / inference
        y_pred = [model(inp) for inp in x]
        loss_val = mse_loss(y_pred, y_true)
        print(epoch+1, loss_val.value)

        # zero grad
        optim.zero_grad()
        
        # backward pass
        loss_val.backward()

        # update params
        optim.step()


    # # saving graph of nn as image
    # graph = draw_dot(loss_val)
    # graph.render("nn", format="png", cleanup=True)