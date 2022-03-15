import numpy as np
#from sympy import * 
from matplotlib import pyplot as plt

"""
f es la funcion de la queremos encontrar la realiza
fm la funcion en termnino de x, solo se requiere para el el metodo iteracion  de punto fijo de
df La derivada de la funcion f, para el metodo de Newton
"""
class raices:
    def __init__(self,f, fm=None, df=None):
        self.f=f
        self.df=df
        self.fm=fm

    def _biseccion(self):
        xr,xl=self.xr,self.xl
        f=self.f
        ea=np.abs(xr-xl)/(xr+xl)*100
        xa=(xr+xl)/2
        xm=xa
        Ea,Xa=[ea],[xm]
        _iter=0
        while(ea>self.epsilon and _iter<self.max_iter):
            xa=xm
            if f(xl)*f(xm)<0:
                xr=xm
            elif f(xl)*f(xm)>0:
                xl=xm
            else:
                break
            xm=(xr+xl)/2
            Xa.append(xm)
            ea=np.abs(xm-xa)/xm*100
            Ea.append(ea)
            _iter+=1
        self._Ea,self._Xa,self._iter=Ea,Xa,_iter
        return xm

    def _iteracion_punto_fijo(self):
        Xa,Ea,_iter=[],[],0
        xl=self.xl
        f=self.fm
        xn=f(xl)
        Xa.append(xn)
        ea=np.abs(xn-xl)/xn*100
        Ea.append(ea)
        while(ea>self.epsilon and _iter < self.max_iter):
            xl=xn
            xn=f(xl)
            ea=np.abs(xn-xl)/xn*100
            Xa.append(xn)
            Ea.append(ea)
            _iter=_iter+1
        self._Xa,self._Ea,self._iter=Xa,Ea,_iter
        return xn  
        
    def encuentra_raiz(self,xl, xr=None, epsilon=0.5e-3, method='biseccion', max_iter=100):
        self.xr,self.xl=xr,xl
        self.epsilon=epsilon
        self.method=method
        self.max_iter=max_iter
        if method in ['biseccion', 'falsa_posicion'] and xr==None:
            raise f"Es necesario proporcionar un valor para xr para el metodo de {method}"
        return getattr(self, f"_{self.method}")()

    def plot_limits(self,xl,xr):
        f=self.f
        fig,ax=plt.subplots()
        dx=np.abs(xl-xr)/100
        X=np.arange(xl,xr,dx)
        Y=f(X)
        ax.plot(X,Y)
        ax.hlines(y=0, xmin=xl,xmax=xr, linestyle='--')
        ax.vlines(x=[xl,xr], ymin=np.min(Y),ymax=np.max(Y), linestyle='--', color='r')
        return fig,ax

    
if __name__ == "__main__":
    xl,xr=0,1
    def fm(x):
        return np.exp(-x)
    def f(x):
        return np.exp(-x)-x
    m=raices(f)# instancia de la calse raices 
    x=m.encuentra_raiz(xl,xr) 
    print(f"Biseccion: x={x}, f(x)={f(x)}, iteraciones={m._iter}")
    m1=raices(f,fm=fm) # instacia para usar el metodo de  iteracion de punto fijo
    x=m1.encuentra_raiz(xl,method="iteracion_punto_fijo")
    print(f"Iteracion punto fijo: x={x}, f(x)={f(x)}, iteraciones={m1._iter}")
            
        
