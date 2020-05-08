# Maze_NTP

dependencies required:

1.torch
2.numpy
3.matplotlib



Files Description:

1.Core : Core training and prediction of next program and r

2.TSI : Task specification interpretor/selector to predict next task sequence

3.NTP : runs the complete NTP algorithm incorporating Core and TSI

4.API : Robot API Calls , move up /down / left / right

5.TaskSeqGen: generates task specifications and sequences for training data


-----------------------Example output for NTP------------------------
-------------------------------------------------- 

Running Move to Goal from initial position (0,0) 


Calling Heirarchical Function: tensor([5.6351e-05, 9.9775e-01, 1.0155e-03, 6.8422e-04, 4.4450e-04, 4.6302e-05],
       grad_fn=<SoftmaxBackward>)
moving up
moving up
Human Failure,placing agent at 1,0

moving up
moving up

Calling Heirarchical Function: tensor([5.0786e-05, 1.0388e-03, 1.7616e-04, 9.9807e-01, 5.8839e-04, 7.9558e-05],
       grad_fn=<SoftmaxBackward>)
moving right
moving right
moving right
