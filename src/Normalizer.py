import numpy as np

class Normalizer:
        
    def load(self,maxfile, minfile):
        self.feature_max = np.loadtxt(maxfile)
        self.feature_min = np.loadtxt(minfile)
        
    def fit(self,data):
        data = np.copy(np.array(data, dtype=float))
        
        self.feature_max = np.max(data,axis=0)
        self.feature_min = np.min(data,axis=0)
        
    def normalize(self,data):
        data = np.copy(np.array(data, dtype=float))
        dims = len(data.shape)
        shape = data.shape
        
        for c in range(data.shape[1]):
            col = data[:,c]
            col /= self.feature_max[c] - self.feature_min[c]
        
        return data
    
    def inv_normalize(self,data):
        data = np.copy(np.array(data, dtype=float))
        
        for c in range(data.shape[1]):
            col = data[:,c]
            col *= self.feature_max[c] - self.feature_min[c]
            
        return data