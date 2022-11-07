# Django-PyOTP

- Using Django REST API Framework Token Authentication.
- Using Time-based one-time password (TOTP) with PyOTP library.
  - https://github.com/pyauth/pyotp
- Linkedin Uploaded post about the project:
  - https://www.linkedin.com/feed/update/urn:li:activity:6995195746190798848/

--------------

[+] Run Project:
- Change your current directory to the project. (cd djangoPyOTP)
- python -m venv env
- source env/bin/activate (Linux) or env/bin/activate (Windows)
- pip install -r requirements.txt
- python manage.py runserver 127.0.0.1:8000

-----------------

[+] Ready Implementations:
- Admin account is already registered.
  - Username: omar
  - Email: omar@omar.com
  - Password: omar
  - auth_token: 6dfe417849ad42b39b0b530f066903ec34b5eda7

- Admin account already has MFA enabled and MFA record.

- Using React.js as front-end.
  - Frontend only requests provision url from backend to embed with QRCode which Google Authenticator need to scan.
    - Dummy Example of final provision uri:
      - otpauth://totp/Secure%20App:alice%40google.com?secret=JBSWY3DPEHPK3PXP&issuer=Secure%20App
  - Frontend shows only the QRCode.

- You can read MFA views, urls, and models code in mfa_otp directory (app).
  - Also, check project urls.py (djangoPyOTP/urls.py)

-----------

[+] Try out:
- Scanning QRCode using Google Authenticator.
- Send POST request to VerifyOTP view "http://127.0.0.1:8000/mfa/verify-otp/"
using Postman or curl with:
  - headers> {"Content-Type": "application/json", "Authorization": Token auth_token}
  - json body> {"otp": "Google Authenticator otp"}

- React app directory is included, if you made changes in react code:
  - npm run build
  - replace new build/ with djangoPyOTP/build
