3. Manage Super Admin
***********************


3.1 View Super admin
======================

**Flow:**

    * Where system admin lands on this screen, frontend have to show list of super admins with as below options:
        * Add button
            * onclick should navigate to the add super admin screen
        * List of super admins:
            * Name
            * Created at
            * status
            * Action 
                * Edit - (Button)
                    * Onclick should navigate to edit screen

                * Delete - (Button)
                    * Onclick should call the delete api
        
    * When view super admin API called, backend perform the below
        * Verify the auth token. For token verification to Refer :ref:`Token_verify`.
        * If valid user
            * Find all super admins from the database.
            * If no super admin found, return empty list.
            * Return success response with success message :ref:`s-10013` and list of super admins.
        
    
    * If any error response is received, frontend displays the error message as an auto-dismissible toast message.

**API:**

    .. note::

        This api is only accessible for system admin only.
    

    * End Point: api/v1/gps/super-admin
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
                    super_admins: [
                        {
                            _id: ObjectId,
                            name: string,
                            status: string,
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


1.2 Add Super admin
======================

**Flow:**

    * Where system admin clicks on add button from the view super admins list screen, frontend have to show below fields:
        * Name - (Text field)
        * Status - (Toggle)
        * Email - (Text field)
        * Photo - (File)
        
    * When Add super admin API called, backend perform the below
        * Verify the auth token. For token verification to Refer :ref:`Token_verify`.
        * If valid user
            * Create the super admin.
            * Return success response with success message :ref:`s-10014`.
        
    
    * If any error response is received, frontend displays the error message as an auto-dismissible toast message.

**API:**

    .. note::

        This api is only accessible for system admin only.
    

    * End Point: api/v1/gps/super-admin
    * Method: POST
    * Default Header: application/json 
    * Auth Header: JWT token
    * Payload:

        .. code-block:: text

                {
                    first_name: string,
                    last_name: string,
                    email_id: string,
                    photo: File,
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


1.3 Update Super admin
======================

**Flow:**

    * Where system admin clicks on edit button from the actions button in view super admins list screen, frontend have to show below fields:
        * Name - (Text field)
        * Status - (Toggle)
        * Email - (Text field)
        * Photo - (File)
        
    * When update super admin API called, backend perform the below
        * Verify the auth token. For token verification to Refer :ref:`Token_verify`.
        * If valid user
            * find the super admin by _id and update.
            * Return success response with success message :ref:`s-10015` and list of super admins.
        
    
    * If any error response is received, frontend displays the error message as an auto-dismissible toast message.

**API:**

    .. note::

        This api is only accessible for system admin only.
    

    * End Point: api/v1/gps/super-admin
    * Method: PATCH
    * Default Header: application/json 
    * Auth Header: JWT token
    * Payload:

        .. code-block:: text

                {
                    _id: Objectid
                    first_name: string,
                    last_name: string,
                    email_id: string,
                    photo: File, 
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



1.4 Delete Super admin
======================

**Flow:**

    * Where system admin clicks on delete button from the actions button in view super admins list screen, frontent should call the delete super admins api.
       
    * When update super admin API called, backend perform the below
        * Verify the auth token. For token verification to Refer :ref:`Token_verify`.
        * If valid user
            * find the super admin by _id and delete.
            * Return success response with success message :ref:`s-10016` and list of super admins.
        
    
    * If any error response is received, frontend displays the error message as an auto-dismissible toast message.

**API:**

    .. note::

        This api is only accessible for system admin only.
    

    * End Point: api/v1/gps/super-admin
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

