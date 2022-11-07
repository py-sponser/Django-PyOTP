from urllib.parse import quote, urlencode


def build_uri(secret, name, issuer):
    """
    Returns the provisioning URI for the OTP; works for either TOTP or HOTP.

    This can then be encoded in a QR Code and used to provision the Google
    Authenticator app.

    See also:
        https://github.com/google/google-authenticator/wiki/Key-Uri-Format

    :param secret: the hotp/totp secret used to generate the URI
    :param name: name of the account
    :param issuer: the name of the OTP issuer; this will be the
        organization title of the OTP entry in Authenticator
    :returns: provisioning uri
    """

    otp_type = "totp"
    base_uri = "otpauth://{0}/{1}?{2}"

    url_args = {"secret": secret}

    label = quote(name)
    if issuer is not None:
        label = quote(issuer) + ":" + label
        url_args["issuer"] = issuer


    uri = base_uri.format(otp_type, label, urlencode(url_args).replace("+", "%20"))
    return uri
