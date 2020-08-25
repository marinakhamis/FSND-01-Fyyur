1. To get the project up and running, set up the requirements 

```
pip3 install -r requirements.txt
```

Didn't work ? 
- Set up the requirements in the Virtualenv 

 1. Set up the venv 
    ```
    $ mkdir myproject
    $ cd myproject
    $ python3 -m venv venv
    ```
    On Windows:
    ```
    > py -3 -m venv venv
    ```
2. Activate the environment
    ```
    $ . venv/bin/activate
    ```

    On Windows:
    ```
    > venv\Scripts\activate
    ```
3. Run this command inside the (venv)

    ```
    pip3 install -r requirements.txt
    ```



