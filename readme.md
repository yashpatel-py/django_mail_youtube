# Mail Project

### Steps To run the project

1. Clone this project
2. Open this project in VsCode or any other code editor.
3. Create vierual environment where `manage.py` in present

    ```text
    # command to create virtual environmtnt
    python -m venv env
    ```

4. Activate virtual environment
    ```
    env/Script/activate
    ```

5. Install packages from `requirements.txt` using below command
    ```
    pip install -r requirements.txt
    ```

6. Run command
    ```
    python manage.py makemigrations

    python manage.py migrate
    ```

7. To run server run bellow command
    ```
    python manage.py runserver
    ```