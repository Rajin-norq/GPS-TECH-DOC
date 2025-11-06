2. Manage Feature
***********************


2.1 View Feature
======================

**Flow:**

    * Where system admin lands on this screen, frontend have to show list of features with as below options:
        * Add button
            * onclick should navigate to the add feature screen
        * List of features:
            * Feature
            * Created at
            * status
            * Action 
                * Edit - (Button)
                    * Onclick should navigate to edit screen

                * Delete - (Button)
                    * Onclick should call the delete api
        
    * When view feature API called, backend perform the below
        * Verify the auth token. For token verification to Refer :ref:`Token_verify`.
        * If valid user
            * Find all features from the database.
            * If no feature found, return empty list.
            * Return success response with success message :ref:`s-10009` and list of features.
        
    
    * If any error response is received, frontend displays the error message as an auto-dismissible toast message.

**API:**

    .. note::

        This api is only accessible for system admin only.
    

    * End Point: api/v1/gps/features
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
                    features: [
                        {
                            _id: ObjectId,
                            name: string,
                            status: string,
                            is_enabled:boolean,
                            is_enabled_controls: boolean,
                            controls:{
                                max_creation_limit: boolean,  
                                duration: boolean,
                                time_limit: boolean,      
                                edit: boolean,
                                max_assigning_limit: boolean,
                            }                                          
                        
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


2.2 Add Feature
======================

**Flow:**

    * Where system admin clicks on add button from the view features list screen, frontend have to show below fields:
        * Name - (Text field)
        * Status - (Toggle)
        * Is Enabled - (Toggle)
            * If isenabled is true the need to show the following  options: 

            * Is Enable Controls - (Toggle)
                * If isEnableControls true then need to show the below fields
                * Max Creation Limit - (Toggle)
                * Duration  - (Toggle)
                * Time Limit  - (Toggle)
                * Edit - (Toggle)
                * Max Assigning Limit - (Toggle)

        
    * When Add feature API called, backend perform the below
        * Verify the auth token. For token verification to Refer :ref:`Token_verify`.
        * If valid user
            * Create the feature.
            * Return success response with success message :ref:`s-10010`.
        
    
    * If any error response is received, frontend displays the error message as an auto-dismissible toast message.

**API:**

    .. note::

        This api is only accessible for system admin only.
    

    * End Point: api/v1/gps/features
    * Method: POST
    * Default Header: application/json 
    * Auth Header: JWT token
    * Payload:

        .. code-block:: text

                {
                    name: string,
                    status: string,
                    is_enabled:boolean,
                    is_enabled_controls: boolean,
                    controls:{
                        max_creation_limit: boolean,  
                        duration: boolean,
                        time_limit: boolean,      
                        edit: boolean,
                        max_assigning_limit: boolean,
                    }  
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


3.3 Update Feature
======================

**Flow:**

    * Where system admin clicks on edit button from the actions button in view features list screen, frontend have to show below fields:
        * Name - (Text field)
        * Status - (Toggle)
        * Is Enabled - (Toggle)
            * If isenabled is true the need to show the following  options: 

            * Is Enable Controls - (Toggle)
                * If isEnableControls true then need to show the below fields
                * Max Creation Limit - (Toggle)
                * Duration  - (Toggle)
                * Time Limit  - (Toggle)
                * Edit - (Toggle)
                * Max Assigning Limit - (Toggle)

        
    * When update feature API called, backend perform the below
        * Verify the auth token. For token verification to Refer :ref:`Token_verify`.
        * If valid user
            * find the feature by _id and update.
            * Return success response with success message :ref:`s-10011` and list of features.
        
    
    * If any error response is received, frontend displays the error message as an auto-dismissible toast message.

**API:**

    .. note::

        This api is only accessible for system admin only.
    

    * End Point: api/v1/gps/features
    * Method: PATCH
    * Default Header: application/json 
    * Auth Header: JWT token
    * Payload:

        .. code-block:: text

                {
                    _id: Objectid
                    name: string,
                    status: string,
                    is_enabled:boolean,
                    is_enabled_controls: boolean,
                    controls:{
                        max_creation_limit: boolean,  
                        duration: boolean,
                        time_limit: boolean,      
                        edit: boolean,
                        max_assigning_limit: boolean,
                    }  
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



2.4 Delete Feature
======================

**Flow:**

    * Where system admin clicks on delete button from the actions button in view features list screen, frontent should call the delete features api.
       
    * When update feature API called, backend perform the below
        * Verify the auth token. For token verification to Refer :ref:`Token_verify`.
        * If valid user
            * find the feature by _id and delete.
            * Return success response with success message :ref:`s-10007` and list of features.
        
    
    * If any error response is received, frontend displays the error message as an auto-dismissible toast message.

**API:**

    .. note::

        This api is only accessible for system admin only.
    

    * End Point: api/v1/gps/features
    * Method: DELETE
    * Default Header: application/json 
    * Auth Header: JWT token
    * Params:

        .. code-block:: text

                {
                    _id: Objectid
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

