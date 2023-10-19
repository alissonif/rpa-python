#!pip install keyboard

# In[ ]:


def escrever():
    import time
    import keyboard

    keyboard.press_and_release('alt+tab')
    time.sleep(1)
    # redação
    texto = """"
    coloque o texto grande aqui
    """
    keyboard.write(texto, delay=0.01)


# In[ ]:

escrever()
