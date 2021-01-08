import numpy as np
def train_test_split(data, params , split):
    split = 1-split
    n_split = int(len(data)*split)
    d_list = [[d,p] for d,p in zip(data, params)]
    d_list = np.asarray(d_list)
    np.random.shuffle(d_list)
    d_list_train = d_list[:n_split,:]
    d_list_test = d_list[n_split:,:]

    train_data = d_list_train[:,0]
    train_data = np.asarray([t for t in train_data])
    test_data = d_list_test[:,0]
    test_data = np.asarray([t for t in test_data])
    
    train_p = d_list_train[:,1]
    train_p = np.asarray([t for t in train_p])

    test_p = d_list_test[:,1]
    test_p = np.asarray([t for t in test_p])

    return (train_data , train_p) , (test_data , test_p)

def model_score(model , data , params , plot=False , epochs = 20 , verbose = 0):

    def plot_loss(history):
        plt.plot(history.history['loss'], label='train loss')
        plt.plot(history.history['val_loss'], label='val_loss')
        #plt.ylim([0, 10])
        plt.xlabel('Epoch')
        plt.ylabel('Error [MPG]')
        plt.legend()
        plt.grid(True)
        plt.show()

    (train_data, train_p) , ( test_data , test_p) = train_test_split(data , params , 0.2)

    history = model.fit(train_data, train_p,validation_split=0.2, epochs=epochs , verbose=verbose)

    if(plot):
        plot_loss(history)

    y_true_test = np.copy(test_p)
    y_pred_test = model.predict(test_data)

    y_true_train = np.copy(train_p)
    y_pred_train = model.predict(train_data)
    mse_train = mean_squared_error(y_true_train, y_pred_train)
    mse_test = mean_squared_error(y_true_test, y_pred_test)
    model.summary()
    return mse_train , mse_test 