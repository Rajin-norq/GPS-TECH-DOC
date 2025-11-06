04. Common 
********************

.. _Token_verify:

4.1. Token Verification
=========================

**Flow:**

    * When API called, backend perform the below
         * Verify the auth token.
            * If invalid auth token, backend returns error :ref:`E-10003`.
            * If expired auth token, backend returns error :ref:`E-10002`.
    
**API:**
    .. note::

        This api is available for all authenticated users. The user to be identified by the JWT token data


    * Request type: All


**Error Scenario:**
                
    * Any unhandled error or server related error. :ref:`E-10001`


     
