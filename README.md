# Installing Dependencies

These files have dependencies including: tkinter, matplotlib, scipy, sv_ttk, PyAstronomy, sgp4.

# Tkinter install

```brew install python-tk```

# Other installs
For matplotlib, scipy, sv_ttk, PyAstronomy, and sgp4.
I ran these installs in a virtual environment.

1. Set up the virtual environment. Within your project directory, open terminal and enter:
```python3 -m venv <pick_VM_name>  ```

2. Activate the environment, telling your computer to "look there" for the files.
Mac Users:
```source <pick_VM_name>/bin/activate ```
Windows Users:
```.\\<pick_VM_name>\Scripts\activate.bat```

3. Install the dependency in the new virtual environment:
```pip3 install matplotlib```

4. Check your install
```pip3 list```

5. When you're done, deactivate the virtual environment
```deactivate```

6. To restart the environment, repeat step 2 within your project directory

## Windows Execution Notes
When running files through the VM, enter the directory of the VM and run the following:
```python ../<finalProjectFolder>/<finalProjectFile>.py```
