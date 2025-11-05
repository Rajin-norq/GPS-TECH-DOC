1. Manage subscription
***********************


1.1 View subscriptions
======================

**Flow:**

    * Where super admin lands on this screen, frontend have to show list of subscriptions with as below options:
        * Add button
            * onclick should navigate to the add subscription screen
        * List of subscriptions:
            * subscription
            * Price
            * Currency
            * status
            * Action 
                * Edit - (Button)
                    * Onclick should navigate to edit screen
                * View - (Button)
                    * Onclick should navigate to subscription details screen
                * Delete - (Button)
                    * Onclick should call the delete api
        
    * When view subscription API called, backend perform the below
        * Verify the auth token. For token verification to Refer .
        * If valid user
            * If any required fields are missing, return error response with similar error which is mentioned in frontend.
            * Send email to every admin with given subject and body.
            * If user data did not exist name or phone,. then update in user data.
            * Return success response with code
    
    * If any error response is received, frontend displays the error message as an auto-dismissible toast message.

    * If backend send success response, frontend perform as below
        * Displays the success message as an auto-dismissible toast message


**API:**

    .. note::

        This api is only accessible for super admin only.
    

    * End Point: api/v1/gps/subscription
    * Method: GET
    * Default Header: application/json 
    * Auth Header: JWT token
    


    * Success Response:

        .. code-block:: text

            {
                status: 'success',
                status_code: 'S-10...',
            }


    * Error Response:

        .. code-block:: text

            {
                status: 'error',
                status_code: 'E-10...'
            }
