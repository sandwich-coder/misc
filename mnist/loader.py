from environment import *
logger = logging.getLogger(name = __name__)
from torchvision.datasets import EMNIST, FashionMNIST
from torchvision.transforms import ToTensor


class Loader:
    def __init__(self):
        pass
    def __repr__(self):
        return 'loader'

    def load(self, name, train = True):
        if not isinstance(name, str):
            raise TypeError('The name should be a string.')
        if not isinstance(train, bool):
            raise TypeError('\'train\' should be boolean.')
        if not train:
            kind = 'test'
        else:
            kind = 'train'

        if name == 'cloths':
            array = FashionMNIST(
                root = 'datasets',
                train = train,
                download = True,
                transform = ToTensor(),
                ).data.numpy()
            array = array.astype('float64')
            array = array.reshape([array.shape[0], -1])
            array = (array - array.min()) / (array.max() - array.min())
            array = (array - np.float64(0.5)) * np.float64(2)
            logger.info('\'{name}\' ({kind}) is loaded.'.format(
                name = name,
                kind = kind,
                ))
            return array

        array = EMNIST(
            root = 'datasets',
            split = name,
            train = train,
            download = True,
            transform = ToTensor(),
            ).data.numpy()
        array = array.astype('float64')

        #image rotation
        array = array.transpose(0, 2, 1)

        array = array.reshape([array.shape[0], -1])
        array = (array - array.min()) / (array.max() - array.min())
        array = (array - np.float64(0.5)) * np.float64(2)

        logger.info('\'{name}\' ({kind}) is loaded.'.format(
            name = name,
            kind = kind,
            ))

        return array
