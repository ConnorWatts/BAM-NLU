from model.utils import get_model
from losses.utils import get_loss
from data.utils import get_dataloader

class ModelRunner(object):

    """Class for training/evaluating models."""

    def __init__(self, config) -> None:

        # could make runner config
        self.start_epoch = config['start_epoch']
        self.total_epoch = config['total_epoch']

        self.model = get_model(config)
        self.loss = get_loss(config)
        self.train_dataloader, self.test_dataloader, self.valid_dataloader = get_dataloader(config)
        self.optimizer = get_optimizer(config)


    def train(self):

        for epoch in range(self.start_epoch,self.total_epoch):
            # print summary
            # poss change LR
            eval_epoch = self.train_epoch(self.train_dataloader,self.model,self.loss,self.optimizer,epoch)
            # eval and poss save

        pass

    def train_epoch(self,train_dataloader,model,loss,optimizer,epoch):

        pass

