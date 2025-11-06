1. Manage Platform
***********************


1.1 View Platform
======================

**Flow:**

    * Where system admin lands on this screen, frontend have to show list of platforms with as below options:
        * Add button
            * onclick should navigate to the add platform screen
        * List of platforms:
            * Platform
            * Created at
            * status
            * Action 
                * Edit - (Button)
                    * Onclick should navigate to edit screen
                * Delete - (Button)
                    * Onclick should call the delete api
        
    * When view platform API called, backend perform the below
        * Verify the auth token. For token verification to Refer :ref:`Token_verify`.
        * If valid user
            * Find all platforms from the database.
            * If no platform found, return empty list.
            * Return success response with success message :ref:`s-10005` and list of platforms.
        
    
    * If any error response is received, frontend displays the error message as an auto-dismissible toast message.

**API:**

    .. note::

        This api is only accessible for system admin only.
    

    * End Point: api/v1/gps/platforms
    * Method: GET
    * Default Header: application/json 
    * Auth Header: JWT token
    * Params:

        .. code-block::text

            {
                page:string;
                search:string
            }


    * Success Response:

        .. code-block:: text

            {
                isStatus: true,
                message: 's-10...',
                data:{
                    platforms: [
                        {
                            _id: ObjectId,
                            name: string,
                            status: string,
                            features: [string], // send the type
                        },
                    ]
                    current_page: number,
                    total_count: number,
                }
            }


    * Error Response:

        .. code-block:: text

            {
                isStatus: false,
                message : 'E-10...'
            }


1.2 Add Platform
======================

**Flow:**

    * Where system admin clicks on add button from the view platforms list screen, frontend have to show below fields:
        * Name - (Text field)
        * Status - (Toggle)
        * Features - (Dropdown)

        
    * When Add platform API called, backend perform the below
        * Verify the auth token. For token verification to Refer :ref:`Token_verify`.
        * If valid user
            * Create the platform.
            * Return success response with success message :ref:`s-10006`.
        
    
    * If any error response is received, frontend displays the error message as an auto-dismissible toast message.

**API:**

    .. note::

        This api is only accessible for system admin only.
    

    * End Point: api/v1/gps/platforms
    * Method: POST
    * Default Header: application/json 
    * Auth Header: JWT token
    * Payload:

        .. code-block:: text

                {
                  name:string  // required,
                  status: string    //required,
                  features: [string] // required send the type
                }


    * Success Response:

        .. code-block:: text

            {
                isStatus: true,
                message: 's-10...',
                data:{
                    platforms: [
                        {
                            _id: ObjectId,
                            name: string,
                            status: string,
                            features: [string], // send the type
                        },
                    ]
                    current_page: number,
                    total_count: number,
                }
            }


    * Error Response:

        .. code-block:: text

            {
                isStatus: false,
                message : 'E-10...'
            }


1.3 Edit Platform
======================

**Flow:**

    * Where system admin clicks on edit button from the actions button in view platforms list screen, frontend have to show below fields:
        * Name - (Text field)
        * Status - (Toggle)
        * Features - (Dropdown)

        
    * When update platform API called, backend perform the below
        * Verify the auth token. For token verification to Refer :ref:`Token_verify`.
        * If valid user
            * Find the platform by the _id and update.
            * Return success response with success message :ref:`s-10007` and list of platforms.
        
    
    * If any error response is received, frontend displays the error message as an auto-dismissible toast message.

**API:**

    .. note::

        This api is only accessible for system admin only.
    

    * End Point: api/v1/gps/platforms
    * Method: PATCH
    * Default Header: application/json 
    * Auth Header: JWT token
    * Payload:

        .. code-block:: text

                {
                  _id: Objectid
                  name:string  // required,
                  status: string    //required,
                  features: [string] // required send the type
                }

    


    * Success Response:

        .. code-block:: text

            {
                isStatus: true,
                message: 's-10...',
                data:{
                    platforms: [
                        {
                            _id: ObjectId,
                            name: string,
                            status: string,
                            features: [string], // send the type
                        },
                    ]
                    current_page: number,
                    total_count: number,
                }
            }


    * Error Response:

        .. code-block:: text

            {
                isStatus: false,
                message : 'E-10...'
            }


1.4 Delete Platform
======================

**Flow:**

    * Where system admin clicks on delete button from the actions button in view platforms list screen, frontend have to show confirmation model
    * After the confirmation from the system admin then frontend calls the delete platform api.


        
    * When delete platform API called, backend perform the below
        * Verify the auth token. For token verification to Refer :ref:`Token_verify`.
        * If valid user
            * find the platforms and update.
            * Return success response with success message :ref:`s-10008` and list of platforms.
        
    
    * If any error response is received, frontend displays the error message as an auto-dismissible toast message.

**API:**

    .. note::

        This api is only accessible for system admin only.
    

    * End Point: api/v1/gps/platforms
    * Method: DELETE
    * Default Header: application/json 
    * Auth Header: JWT token
    * Payload:

        .. code-block:: text

                {
                  _id: Objectid
                  name:string  // required,
                  status: string    //required,
                  features: [string] // required send the type
                }

    


    * Success Response:

        .. code-block:: text

            {
                isStatus: true,
                message: 's-10...',
                data:{
                    platforms: [
                        {
                            _id: ObjectId,
                            name: string,
                            status: string,
                            features: [string], // send the type
                        },
                    ]
                    current_page: number,
                    total_count: number,
                }
            }


    * Error Response:

        .. code-block:: text

            {
                isStatus: false,
                message : 'E-10...'
            }


