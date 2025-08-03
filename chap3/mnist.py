from sklearn.datasets import fetch_openml
import matplotlib.pyplot as plt

mnist = fetch_openml('mnist_784', as_frame=False)

X,y = mnist.data, mnist.target

print(X)

print(X.shape)
print(y.shape)

def plot_mnist(image_data):
    image = image_data.reshape(28,28)
    plt.imshow(image,cmap='binary')
    plt.axis('off')

plot_mnist(X[0])
plt.show()

print(y[0])