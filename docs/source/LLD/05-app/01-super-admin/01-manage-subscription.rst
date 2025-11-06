1. Manage subscription
***********************


1.1 View subscriptions
=======================

**Flow:**

    * Where super admin lands on this screen, frontend have to show list of subscriptions with as below options:
        * Add button
            * onclick should navigate to the add subscription screen
        * Search bar
        * List of subscriptions:
            * subscription
            * Price
            * Currency
            * status
            * Action 
                * Edit - (Button)
                    * Onclick should navigate to edit screen
                * Delete - (Button)
                    * Onclick should call the delete api
            * Pagination
           
    * When view subscription API called, backend perform the below
        * Verify the auth token. For token verification to Refer :ref:`Token_verify`.
        * If valid user
            * find all subscriptions from the database.
            * If no subscriptions found, return empty list.
            * Return success response with success message :ref:`s-10001`
              
        
    
    * If any error response is received, frontend displays the error message as an auto-dismissible toast message.

**API:**

    .. note::

        This api is only accessible for super admin only.
    

    * End Point: api/v1/gps/subscription
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
                    subscriptions: [
                        {
                            _id: ObjectId,
                            name: string,
                            price: number,
                            currency: string,
                            status: string,
                            features: [   
                                {
                                    _id:ObjectId,
                                    type: string,           
                                    is_enabled: boolean,    
                                    is_enable_controls: boolean,
                                    controls :{
                                        max_creation_limit: number,  
                                        duration: string,
                                        time_limit: string,      
                                        edit: boolean,
                                        max_assigning_limit: number,
                                    }
                                  
                                }
                            ],
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



1.2 Add subscriptions
======================

**Flow:**

    * Where super admin lands on this screen, frontend have to show below fields:
        * Name (Text field)
        * Price (Number field)
        * Currency (Dropdown)
        * Status (Dropdown - Active/Inactive)
        * Auto renew (Toggle)
        * Features -  :ref:`features`
            * Super admin will see the list of features assigned.
            * Driver
                * Enable/Disable (Toggle)
                * Enable controls: (Toggle)
                    * If enable controls is enabled, show below fields.
                    * Max creation limit (Number field).

             * Vehicle
                * Enable/Disable (Toggle)
                * Enable controls: (Toggle)
                    * If enable controls is enabled, show below fields.
                    * Max creation limit (Number field).

            * Reports
                * Enable/Disable (Toggle)
                * Enable controls: (Toggle)
                    * If enable controls is enabled, show below fields.
                    * Max creation limit (Number field)
                    * Duration (text field - :ref:`duration`)
                    * Time limit (Dropdown - :ref:`time_limit`)

            * Event Rule
                * Enable/Disable (Toggle)
                * Enable controls: (Toggle)
                    * If enable controls is enabled, show below fields.
                    * Max creation limit (Number field).
                    * Duration (text field - :ref:`duration`).
                    * Time limit (Dropdown - :ref:`time_limit`).

            * Dashboard
                * Enable/Disable (Toggle)
                * Enable controls: (Toggle)
                    * If enable controls is enabled, show below fields.
                    * Duration (text field - :ref:`duration`).
                    * Time limit (Dropdown - :ref:`time_limit`).

            * Geofence
                * Enable/Disable (Toggle)
                * Enable controls: (Toggle)
                    * If enable controls is enabled, show below fields.
                    * Max creation limit (Number field)

            * Geofence Group
                * Enable/Disable (Toggle)
                * Enable controls: (Toggle)
                    * If enable controls is enabled, show below fields.
                    * Max creation limit (Number field)

            * Point of Interest
                * Enable/Disable (Toggle)
                * Enable controls: (Toggle)
                    * If enable controls is enabled, show below fields.
                    * Max creation limit (Number field)

            * POI Category
                * Enable/Disable (Toggle)
                * Enable controls: (Toggle)
                    * If enable controls is enabled, show below fields.
                    * Max creation limit (Number field)

            * Device Mapper
                * Enable/Disable (Toggle)
                * Enable controls: (Toggle)
                    * If enable controls is enabled, show below fields.
                    * Edit (Toggle)

            * Users
                * Enable/Disable (Toggle)
                * Enable controls: (Toggle)
                    * If enable controls is enabled, show below fields.
                    * Max creation limit (Number field)

            * Tags
                * Enable/Disable (Toggle)
                * Enable controls: (Toggle)
                    * If enable controls is enabled, show below fields.
                    * Max creation limit (Number field)
                    * Max Assigning Limit (Number field)

            * Roles and privileges
                * Enable/Disable (Toggle)
                * Enable controls: (Toggle)
                    * If enable controls is enabled, show below fields.
                    * Max creation limit (Number field)

            * Api sharing
                * Enable/Disable (Toggle)
                * Enable controls: (Toggle)
                    * If enable controls is enabled, show below fields.
                    * Max creation limit (Number field)

      
        * Save button
            * Onclick should call the add subscription api
        
    * When Add subscription API called, backend perform the below
        * Verify the auth token. For token verification to Refer :ref:`Token_verify`.  
        * If valid user
            * Create the subscription.
            * Return success response with success message :ref:`s-10002`.
        
    
    * If any error response is received, frontend displays the error message as an auto-dismissible toast message.

**API:**

    .. note::

        This api is only accessible for super admin only.
    

    * End Point: api/v1/gps/subscription
    * Method: POST
    * Default Header: application/json 
    * Auth Header: JWT token
    * Payload:
        .. code-block:: text

            {
                name: string,     // required
                price: number,   // required
                currency: string, // required
                status: string,   // required   
                features: [
                    {
                        type: string,           // required - enum(1.3)
                        is_enabled: boolean,    
                        is_enable_controls: boolean,
                        max_creation_limit: number,  
                        duration: string,
                        time_limit: string,      
                        edit: boolean,
                        max_assigning_limit: number,
                    }
                ],
            }


    * Success Response:

        .. code-block:: text

            {
                isStatus: true,
                message: 's-10...',
              
            }


    * Error Response:

        .. code-block:: text

            {
                isStatus: false,
                message : 'E-10...'
            }




1.3 Update subscriptions
==========================

**Flow:**

    * Where super admin clicks on the edit button from the actions button, frontend have to show below fields:
        * Name (Text field)
        * Price (Number field)
        * Currency (Dropdown)
        * Status (Dropdown - Active/Inactive)
        * Auto renew (Toggle)
        * Features -  :ref:`features`
            * Super admin will see the list of features assigned.
            * Driver
                * Enable/Disable (Toggle)
                * Enable controls: (Toggle)
                    * If enable controls is enabled, show below fields.
                    * Max creation limit (Number field).

             * Vehicle
                * Enable/Disable (Toggle)
                * Enable controls: (Toggle)
                    * If enable controls is enabled, show below fields.
                    * Max creation limit (Number field).

            * Reports
                * Enable/Disable (Toggle)
                * Enable controls: (Toggle)
                    * If enable controls is enabled, show below fields.
                    * Max creation limit (Number field)
                    * Duration (text field - :ref:`duration`)
                    * Time limit (Dropdown - :ref:`time_limit`)

            * Event Rule
                * Enable/Disable (Toggle)
                * Enable controls: (Toggle)
                    * If enable controls is enabled, show below fields.
                    * Max creation limit (Number field).
                    * Duration (text field - :ref:`duration`).
                    * Time limit (Dropdown - :ref:`time_limit`).

            * Dashboard
                * Enable/Disable (Toggle)
                * Enable controls: (Toggle)
                    * If enable controls is enabled, show below fields.
                    * Duration (text field - :ref:`duration`).
                    * Time limit (Dropdown - :ref:`time_limit`).

            * Geofence
                * Enable/Disable (Toggle)
                * Enable controls: (Toggle)
                    * If enable controls is enabled, show below fields.
                    * Max creation limit (Number field)

            * Geofence Group
                * Enable/Disable (Toggle)
                * Enable controls: (Toggle)
                    * If enable controls is enabled, show below fields.
                    * Max creation limit (Number field)

            * Point of Interest
                * Enable/Disable (Toggle)
                * Enable controls: (Toggle)
                    * If enable controls is enabled, show below fields.
                    * Max creation limit (Number field)

            * POI Category
                * Enable/Disable (Toggle)
                * Enable controls: (Toggle)
                    * If enable controls is enabled, show below fields.
                    * Max creation limit (Number field)

            * Device Mapper
                * Enable/Disable (Toggle)
                * Enable controls: (Toggle)
                    * If enable controls is enabled, show below fields.
                    * Edit (Toggle)

            * Users
                * Enable/Disable (Toggle)
                * Enable controls: (Toggle)
                    * If enable controls is enabled, show below fields.
                    * Max creation limit (Number field)

            * Tags
                * Enable/Disable (Toggle)
                * Enable controls: (Toggle)
                    * If enable controls is enabled, show below fields.
                    * Max creation limit (Number field)
                    * Max Assigning Limit (Number field)

            * Roles and privileges
                * Enable/Disable (Toggle)
                * Enable controls: (Toggle)
                    * If enable controls is enabled, show below fields.
                    * Max creation limit (Number field)

            * Api sharing
                * Enable/Disable (Toggle)
                * Enable controls: (Toggle)
                    * If enable controls is enabled, show below fields.
                    * Max creation limit (Number field)

      
        * Save button
            * Onclick should call the add subscription api
        
    * When Update subscription API called, backend perform the below
    * Verify the auth token. For token verification to Refer :ref:`Token_verify`.
        * If valid user
            * Find the subscription and update the subscription.
            * Return success response with success message :ref:`s-10003`.


    * If any error response is received, frontend displays the error message as an auto-dismissible toast message.

**API:**

    .. note::

        This api is only accessible for super admin only.
    

    * End Point: api/v1/gps/subscription
    * Method: PATCH
    * Default Header: application/json 
    * Auth Header: JWT token
    * Payload:
        .. code-block:: text

            {
                _id: ObjectId,   // required
                name: string,     // required
                price: number,   // required
                currency: string, // required
                status: string,   // required   
                features: [
                    {
                        type: string,           // required - enum(1.3)
                        is_enabled: boolean,    
                        is_enable_controls: boolean,
                        max_creation_limit: number,  
                        duration: string,
                        time_limit: string,      
                        edit: boolean,
                        max_assigning_limit: number,
                    }
                ],
            }


    * Success Response:

        .. code-block:: text

            {
                isStatus: true,
                message: 's-10...',
              
            }


    * Error Response:

        .. code-block:: text

            {
                isStatus: false,
                message : 'E-10...'
            }


1.2 Delete subscriptions
==========================

**Flow:**

    * Where super admin clicks on the Delete button from the actions button, frontend have to call delete subscription api        
        
    * When Delete subscription API called, backend perform the below
        * Verify the auth token. For token verification to Refer :ref:`Token_verify`.
        * If valid user
            * Find the subscription and delete the subscription.
            * Return success response with success message :ref:`s-10004`.


    * If any error response is received, frontend displays the error message as an auto-dismissible toast message.

**API:**

    .. note::

        This api is only accessible for super admin only.
    

    * End Point: api/v1/gps/subscription
    * Method: PATCH
    * Default Header: application/json 
    * Auth Header: JWT token
    * Params:
        .. code-block:: text

            {
                _id: ObjectId,   // required
            }


    * Success Response:

        .. code-block:: text

            {
                isStatus: true,
                message: 's-10...',
              
            }


    * Error Response:

        .. code-block:: text

            {
                isStatus: false,
                message : 'E-10...'
            }


