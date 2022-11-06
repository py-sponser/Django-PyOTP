from urllib.parse import quote, urlencode


def build_uri(secret, name, issuer, digits, period):
    """
    Returns the provisioning URI for the OTP; works for either TOTP or HOTP.

    This can then be encoded in a QR Code and used to provision the Google
    Authenticator app.

    For module-internal use.

    See also:
        https://github.com/google/google-authenticator/wiki/Key-Uri-Format

    :param secret: the hotp/totp secret used to generate the URI
    :param name: name of the account
    :param issuer: the name of the OTP issuer; this will be the
        organization title of the OTP entry in Authenticator
    :param algorithm: the algorithm used in the OTP generation.
    :param digits: the length of the OTP generated code.
    :param period: the number of seconds the OTP generator is set to
        expire every code.
    :returns: provisioning uri
    """
    # initial_count may be 0 as a valid param

    # Handling values different from defaults
    # is_algorithm_set = algorithm is not None and algorithm != "sha1"
    is_digits_set = digits is not None and digits != 6
    is_period_set = period is not None and period != 30

    otp_type = "totp"
    base_uri = "otpauth://{0}/{1}?{2}"

    url_args = {"secret": secret}

    label = quote(name)
    if issuer is not None:
        label = quote(issuer) + ":" + label
        url_args["issuer"] = issuer

    # if is_algorithm_set:
    #     url_args["algorithm"] = algorithm.upper()  # type: ignore

    if is_digits_set:
        url_args["digits"] = digits
    if is_period_set:
        url_args["period"] = period

    uri = base_uri.format(otp_type, label, urlencode(url_args).replace("+", "%20"))
    return uri
