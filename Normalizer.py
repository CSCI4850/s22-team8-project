import numpy as np

class Normalizer:
        
        
        
    def load(maxfile, minfile):
        
        self.feature_max = np.loadtxt(maxfile)
        self.feature_min = np.loadtxt(minfile)
        
    
    def fit(self,data):
        data = np.copy(np.array(data, dtype=float))
        
        #if len(data.shape) == 3:
        #    data = data.reshape((-1,data.shape[2]))
        
        
        self.feature_max = np.max(data,axis=0)
        self.feature_min = np.min(data,axis=0)
        
    
    def normalize(self,data):
        data = np.copy(np.array(data, dtype=float))
        dims = len(data.shape)
        shape = data.shape
        
        #if dims == 3:
        #    data = data.reshape((-1,data.shape[2]))
        
        
        for c in range(data.shape[1]):
            col = data[:,c]
            col /= self.feature_max[c] - self.feature_min[c]
            
        #if dims == 3:
        #    data = data.reshape(shape)
        
        return data
    
    
    def inv_normalize(self,data):
        data = np.copy(np.array(data, dtype=float))
        
        #if len(data.shape) == 3:
        #    data = data.reshape((-1,data.shape[2]))
        
        for c in range(data.shape[1]):
            col = data[:,c]
            col *= self.feature_max[c] - self.feature_min[c]
            
        return data