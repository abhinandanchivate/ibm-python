Here is the first batch of ✅ **Advanced REST API MCQs (1–50)** with:

* ✔ Correct answers
* 🧠 Explanations for correct and incorrect options

---

## ✅ **REST MCQs (1–50)**

---

### **Q1. What does REST stand for?**

* A. Remote Execution Standard Tool
* B. Representational State Transfer ✅
* C. Remote Service Technology
* D. Reliable Endpoint Service Tool
  ✔ REST = Representational State Transfer
  ❌ Others are made-up or incorrect expansions.

---

### **Q2. Which HTTP method is idempotent?**

* A. POST
* B. GET ✅
* C. PATCH
* D. CONNECT
  ✔ GET does not change server state.
  ❌ POST creates resources → not idempotent.

---

### **Q3. Which HTTP method is used to update a resource entirely?**

* A. PATCH
* B. PUT ✅
* C. HEAD
* D. OPTIONS
  ✔ PUT replaces the entire resource.
  ❌ PATCH is for partial updates.

---

### **Q4. Which HTTP status code means “Resource created successfully”?**

* A. 200
* B. 202
* C. 201 ✅
* D. 204
  ✔ 201 = Created
  ❌ 200 = OK, 204 = No Content

---

### **Q5. Which HTTP method is NOT safe?**

* A. GET
* B. HEAD
* C. OPTIONS
* D. DELETE ✅
  ✔ DELETE modifies server state
  ❌ Safe = read-only

---

### **Q6. What is HATEOAS in REST?**

* A. Hypermedia As The Engine Of Application State ✅
* B. High Availability API Transfer
* C. Header Access Token Endpoint Auth
* D. Hyper Automation Transfer
  ✔ REST maturity level 3 uses HATEOAS
  ❌ Others are invalid terms

---

### **Q7. Which status code means unauthorized access?**

* A. 500
* B. 403
* C. 401 ✅
* D. 301
  ✔ 401 = Not Authenticated
  ❌ 403 = Forbidden, 301 = Redirect

---

### **Q8. Which method retrieves only headers without a body?**

* A. GET
* B. HEAD ✅
* C. OPTIONS
* D. DELETE
  ✔ HEAD is a lightweight GET
  ❌ GET returns body

---

### **Q9. What is a RESTful resource typically represented as?**

* A. Database record
* B. Service
* C. URI ✅
* D. IP address
  ✔ REST identifies resources using URIs
  ❌ Others describe backend elements

---

### **Q10. What does the OPTIONS method do?**

* A. Sends a request payload
* B. Deletes a resource
* C. Lists available methods ✅
* D. Caches resource
  ✔ OPTIONS tells what methods are allowed
  ❌ Not used for data ops

---

### **Q11. What does 204 No Content mean?**

* A. Success, with a message
* B. Error, no payload
* C. Success, no body ✅
* D. Resource moved
  ✔ 204 = Operation successful, no response body
  ❌ It’s not an error

---

### **Q12. What does 400 Bad Request mean?**

* A. Wrong API version
* B. Resource not found
* C. Syntax error in request ✅
* D. Auth failed
  ✔ 400 = Client sent malformed data
  ❌ 404 = Not Found

---

### **Q13. Which response code is used for a deleted resource?**

* A. 204 ✅
* B. 201
* C. 200
* D. 403
  ✔ 204 = Success, no content left
  ❌ 200 = Still OK with data

---

### **Q14. What is idempotency in REST?**

* A. Returning status codes
* B. Client-side state
* C. Same request = same result ✅
* D. No response needed
  ✔ Idempotency = Repeat request → same effect
  ❌ POST is not idempotent

---

### **Q15. What does a 500 status code indicate?**

* A. Client error
* B. Server error ✅
* C. Timeout
* D. Unauthorized
  ✔ 500 = Internal server error
  ❌ 4xx = Client errors

---

### **Q16. Which method should be used to create a new resource?**

* A. GET
* B. PUT
* C. POST ✅
* D. PATCH
  ✔ POST creates a resource
  ❌ PUT can overwrite if resource exists

---

### **Q17. RESTful services should be...**

* A. Stateful
* B. Stateless ✅
* C. Session-based
* D. Cookie-only
  ✔ REST = No server-side session state
  ❌ State is held on client side

---

### **Q18. REST relies on which protocol?**

* A. FTP
* B. SMTP
* C. HTTP ✅
* D. SSH
  ✔ REST is built on HTTP methods
  ❌ Others are unrelated protocols

---

### **Q19. In REST, the response format is usually...**

* A. PDF
* B. CSV
* C. JSON ✅
* D. HTML
  ✔ JSON is lightweight and widely used
  ❌ HTML is for web pages, not APIs

---

### **Q20. What does 403 Forbidden mean?**

* A. Login required
* B. Resource moved
* C. Access denied ✅
* D. Endpoint gone
  ✔ 403 = Authenticated but not authorized
  ❌ 401 = Auth required

---

### **Q21. What is content negotiation in REST?**

* A. Cache validation
* B. Compression
* C. Requesting format types ✅
* D. Security header
  ✔ REST supports `Accept:` headers for formats
  ❌ Not about authentication

---

### **Q22. Which HTTP method is not idempotent?**

* A. PUT
* B. POST ✅
* C. DELETE
* D. GET
  ✔ POST creates → different response
  ❌ PUT, DELETE, GET are idempotent

---

### **Q23. What does 422 Unprocessable Entity mean?**

* A. Too large
* B. Can't parse request ✅
* C. Database full
* D. Server crash
  ✔ 422 = Request was syntactically okay, but semantically wrong
  ❌ Not a 400 or 500 level error

---

### **Q24. What does RESTful mean?**

* A. Server-driven
* B. Service-oriented
* C. Follows REST constraints ✅
* D. Cookie-enabled
  ✔ RESTful = Follows HTTP, URIs, statelessness
  ❌ Not a buzzword

---

### **Q25. What’s the correct MIME type for JSON?**

* A. application/xml
* B. text/json
* C. application/json ✅
* D. text/plain
  ✔ `application/json` is the correct MIME type
  ❌ Others are incorrect for JSON

---

### **Q26–50 will follow in the next message. Shall I continue?**
Continuing with ✅ **Advanced REST API MCQs (26–50)**

---

### **Q26. What is the purpose of ETag in REST?**

* A. Authentication
* B. Caching validation ✅
* C. Authorization
* D. Encryption
  ✔ ETag helps validate cache freshness.
  ❌ Not related to auth or security.

---

### **Q27. Which HTTP header is used for content negotiation?**

* A. Accept ✅
* B. Content-Type
* C. Location
* D. Range
  ✔ `Accept` header tells server preferred response format.
  ❌ Content-Type defines request payload format.

---

### **Q28. What does the 429 status code indicate?**

* A. Not Found
* B. Too Many Requests ✅
* C. Unavailable
* D. Timeout
  ✔ 429 is returned when rate limit is exceeded.
  ❌ Common in APIs with throttling.

---

### **Q29. What is URI versioning in REST?**

* A. v1, v2 in path ✅
* B. Version header
* C. Token reuse
* D. Session key
  ✔ `/api/v1/resource` is URI versioning.
  ❌ Headers are used in other styles.

---

### **Q30. Which status code is used when the server is down for maintenance?**

* A. 503 ✅
* B. 502
* C. 500
* D. 408
  ✔ 503 = Service Unavailable
  ❌ 502 = Bad Gateway, 408 = Timeout

---

### **Q31. Which authentication method sends token in Authorization header?**

* A. OAuth
* B. Basic Auth
* C. JWT ✅
* D. Digest Auth
  ✔ JWT is passed in `Authorization: Bearer <token>`
  ❌ Others follow different schemes

---

### **Q32. What does a 301 status code indicate?**

* A. Unauthorized
* B. Temporary redirect
* C. Permanent redirect ✅
* D. Retry
  ✔ 301 = Resource permanently moved
  ❌ 302 = Temporary

---

### **Q33. Which HTTP method is used to partially update a resource?**

* A. POST
* B. PUT
* C. PATCH ✅
* D. MERGE
  ✔ PATCH is for partial updates
  ❌ PUT = full replacement

---

### **Q34. Which tool documents REST APIs using annotations?**

* A. Swagger/OpenAPI ✅
* B. Postman
* C. NGINX
* D. JSON Schema
  ✔ Swagger = REST API documentation
  ❌ Postman is for testing

---

### **Q35. What does 304 Not Modified mean?**

* A. Bad request
* B. Modified resource
* C. Resource cached ✅
* D. Retry later
  ✔ 304 indicates cached version is still valid
  ❌ Doesn’t mean resource changed

---

### **Q36. Which header prevents Cross-Origin Requests?**

* A. Content-Type
* B. Authorization
* C. CORS ✅
* D. X-Frame-Options
  ✔ CORS headers manage cross-origin policies
  ❌ Others unrelated to domain requests

---

### **Q37. What’s the default HTTP method if none is specified in an HTML form?**

* A. POST
* B. PUT
* C. GET ✅
* D. DELETE
  ✔ GET is default method in HTML forms
  ❌ Must explicitly define POST

---

### **Q38. What is rate limiting?**

* A. Caching mechanism
* B. Restricting number of requests ✅
* C. Reducing response time
* D. Handling timeout
  ✔ Rate limiting helps prevent abuse
  ❌ Not related to performance boost

---

### **Q39. What’s the purpose of the `Location` header?**

* A. User's region
* B. Auth check
* C. Redirection URI ✅
* D. Gateway
  ✔ Tells the client where a newly created resource resides
  ❌ Not for auth

---

### **Q40. Which status code indicates a conflict in resource state?**

* A. 409 ✅
* B. 404
* C. 410
* D. 403
  ✔ 409 = Conflict (e.g., duplicate submission)
  ❌ Others indicate different issues

---

### **Q41. Which header is used to describe the format of the request body?**

* A. Accept
* B. Content-Type ✅
* C. ETag
* D. Location
  ✔ Content-Type = MIME of the payload
  ❌ Accept is for response

---

### **Q42. What does REST say about session state?**

* A. Required
* B. Optional
* C. Should be stateless ✅
* D. Tokenized
  ✔ REST = Stateless interactions
  ❌ No session on server side

---

### **Q43. Which method should be used to delete a specific resource?**

* A. PUT
* B. POST
* C. DELETE ✅
* D. GET
  ✔ DELETE = remove existing resource
  ❌ Others modify or read

---

### **Q44. Which HTTP verb should return 405 if not supported?**

* A. GET
* B. DELETE
* C. Any unsupported method ✅
* D. PUT
  ✔ 405 = Method Not Allowed
  ❌ Any verb can trigger it if not handled

---

### **Q45. What does RESTful API design recommend for plural resources?**

* A. Singular
* B. Random
* C. Plural ✅
* D. CamelCase
  ✔ e.g., `/users` not `/user`
  ❌ Consistency matters

---

### **Q46. What’s an API gateway?**

* A. Network filter
* B. Reverse proxy for APIs ✅
* C. Database admin tool
* D. JSON parser
  ✔ API gateway handles routing, rate limits, etc.
  ❌ Not for DB or parsing

---

### **Q47. Which response status is best after a successful PUT request?**

* A. 200 ✅
* B. 201
* C. 204
* D. 302
  ✔ 200 = Resource updated
  ❌ 201 = Created (for POST)

---

### **Q48. What does a 415 Unsupported Media Type mean?**

* A. Wrong HTTP method
* B. Expired token
* C. Server can't understand the Content-Type ✅
* D. Resource locked
  ✔ 415 = Payload format not supported
  ❌ Header issue, not method

---

### **Q49. What’s a good REST practice for file uploads?**

* A. Use GET
* B. Use PATCH
* C. Use POST ✅
* D. Use DELETE
  ✔ POST handles new uploads
  ❌ GET = read-only

---

### **Q50. What status code should a GET request return when data is empty but valid?**

* A. 404
* B. 204 ✅
* C. 200
* D. 403
  ✔ 204 = Success, but no content
  ❌ 404 = Not Found, which may be incorrect

---

Continuing with ✅ **Advanced REST API MCQs (51–100)**

---

### **Q51. Which layer handles REST resource URIs?**

* A. Transport
* B. Presentation
* C. Application ✅
* D. Session
  ✔ REST URI routing is part of the application layer.
  ❌ Not part of TCP/IP transport layers.

---

### **Q52. What is the main reason REST gained popularity over SOAP?**

* A. Binary data support
* B. No internet access needed
* C. Lightweight and stateless ✅
* D. Requires WSDL
  ✔ REST is simpler and faster.
  ❌ SOAP is heavier with strict contracts.

---

### **Q53. What HTTP status code represents "Gone"?**

* A. 410 ✅
* B. 404
* C. 403
* D. 301
  ✔ 410 = resource permanently removed.
  ❌ 404 = not found (maybe temporary)

---

### **Q54. Which HTTP method is NOT cacheable?**

* A. GET
* B. HEAD
* C. POST ✅
* D. OPTIONS
  ✔ POST is non-idempotent, so not safely cacheable.
  ❌ GET and HEAD are cacheable.

---

### **Q55. Which technique is commonly used for paginating REST results?**

* A. Caching
* B. Chunking
* C. Query parameters ✅
* D. JWT
  ✔ Use `?page=2&size=20`
  ❌ Not a job for JWT.

---

### **Q56. What is the role of “statelessness” in REST?**

* A. Reuse sessions
* B. Store server state
* C. Client must manage session ✅
* D. Minimize caching
  ✔ Server does not maintain session context.
  ❌ Client stores all state.

---

### **Q57. What is a "resource" in REST context?**

* A. Always a file
* B. A URI ✅
* C. A function
* D. A session
  ✔ Resources are identified using URIs.
  ❌ Not tied to physical files.

---

### **Q58. How is versioning often handled in RESTful APIs?**

* A. PUT headers
* B. File names
* C. URI paths like /v1 ✅
* D. JWT claims
  ✔ Versioning is added in URI: `/api/v1/users`
  ❌ Other methods are uncommon.

---

### **Q59. Which type of authentication uses client ID & secret?**

* A. OAuth 2.0 ✅
* B. Basic Auth
* C. JWT
* D. Digest Auth
  ✔ OAuth 2.0 uses client credentials for flow.
  ❌ Basic uses user\:pass

---

### **Q60. Which response code indicates a redirection that can change over time?**

* A. 302 ✅
* B. 301
* C. 307
* D. 308
  ✔ 302 = Found (Temporary redirect)
  ❌ 301 = Permanent

---

### **Q61. How should you expose relationships in REST?**

* A. Embed DB schema
* B. Return nested resources ✅
* C. Use GraphQL
* D. Split everything
  ✔ REST often returns nested JSON (e.g., orders inside user)
  ❌ Not about schema

---

### **Q62. What is Swagger/OpenAPI used for?**

* A. Testing
* B. Load balancing
* C. Documenting REST APIs ✅
* D. Throttling
  ✔ Swagger = auto-gen docs
  ❌ Not a runtime tool

---

### **Q63. What does 206 Partial Content mean?**

* A. Error
* B. Incomplete upload
* C. Response to range request ✅
* D. Too many requests
  ✔ 206 = Range/streamed responses
  ❌ Not an error

---

### **Q64. Which method is best for replacing a resource?**

* A. POST
* B. PATCH
* C. PUT ✅
* D. DELETE
  ✔ PUT replaces resource fully
  ❌ PATCH updates partially

---

### **Q65. What’s a good way to represent errors in REST API?**

* A. Plain text
* B. JSON with message and code ✅
* C. HTML
* D. 500 for all
  ✔ Standard: `{ "error": "...", "code": 400 }`
  ❌ HTML isn’t machine-friendly

---

### **Q66. Which HTTP header defines request format?**

* A. Accept
* B. Content-Type ✅
* C. Authorization
* D. Allow
  ✔ Tells server format of body
  ❌ Accept is for response

---

### **Q67. What is a REST API resource collection?**

* A. A list of functions
* B. A session list
* C. A group of similar resources ✅
* D. A database
  ✔ E.g., `/users` is a collection
  ❌ REST is not DB-specific

---

### **Q68. Which method is discouraged for non-idempotent operations?**

* A. POST ✅
* B. GET
* C. PUT
* D. DELETE
  ✔ POST creates → not idempotent
  ❌ GET/PUT/DELETE should be idempotent

---

### **Q69. What is the primary benefit of REST being stateless?**

* A. Increased load
* B. Easier scaling ✅
* C. User tracking
* D. Server sessions
  ✔ Stateless → no session tracking
  ❌ Easier for microservices

---

### **Q70. What does a 200 OK response mean?**

* A. Resource created
* B. Resource deleted
* C. Request succeeded ✅
* D. Server down
  ✔ 200 = standard successful response
  ❌ Not specific to resource type

---

### **Q71. What type of response should you send for a HEAD request?**

* A. No body ✅
* B. HTML
* C. JSON
* D. Plain text
  ✔ HEAD = headers only
  ❌ Similar to GET without body

---

### **Q72. How do you indicate pagination metadata in REST?**

* A. Body only
* B. URI only
* C. Response headers ✅
* D. ETag
  ✔ Include `X-Total-Count`, `Link` in headers
  ❌ Not in JWT

---

### **Q73. What is the use of the OPTIONS method?**

* A. Retrieves metadata
* B. Deletes resource
* C. Lists allowed methods ✅
* D. Encrypts request
  ✔ OPTIONS returns `Allow:`
  ❌ Used for CORS preflight

---

### **Q74. Which header indicates client-requested data format?**

* A. Content-Type
* B. Accept ✅
* C. Referer
* D. Expires
  ✔ Accept = client wants JSON/XML/etc
  ❌ Content-Type = request payload

---

### **Q75. Which method should NOT return a body in response?**

* A. POST
* B. GET
* C. HEAD ✅
* D. PUT
  ✔ HEAD responses contain only headers
  ❌ Others return content

---

### **Q76. Which status code signals invalid JWT token?**

* A. 403
* B. 404
* C. 401 ✅
* D. 409
  ✔ 401 = unauthorized
  ❌ 403 = valid login, denied access

---

### **Q77. What does 202 Accepted mean?**

* A. Request failed
* B. Processed
* C. Queued for processing ✅
* D. Not supported
  ✔ Server accepted it but hasn’t completed
  ❌ 200 = completed now

---

### **Q78. What tool allows manual REST testing?**

* A. VS Code
* B. Excel
* C. Postman ✅
* D. Docker
  ✔ Postman is designed for REST testing
  ❌ Not an IDE

---

### **Q79. Which header controls caching behavior?**

* A. X-CACHE
* B. Cache-Control ✅
* C. Expires
* D. Accept
  ✔ `Cache-Control` sets client/server caching
  ❌ Expires is older alternative

---

### **Q80. What’s the difference between 401 and 403?**

* A. 403 = Token expired
* B. 401 = Auth required ✅
* C. 401 = Access granted
* D. Same
  ✔ 401 → login needed
  ❌ 403 → login ok, no access rights

---

Thanks for the confirmation! Let’s continue with ✅ **Advanced REST API MCQs (81–100)** — each with explanations for correct and incorrect answers.

---

### **Q81. What is the purpose of API throttling?**

* A. Speed up requests
* B. Log analytics
* C. Control traffic load ✅
* D. Replace caching
  ✔ Throttling limits request rates to prevent abuse.
  ❌ Not for improving speed or logs.

---

### **Q82. What does a 307 status code mean?**

* A. Moved permanently
* B. Temporary redirect (same method) ✅
* C. Unauthorized
* D. Resource gone
  ✔ 307 preserves method (e.g., POST) in redirect.
  ❌ 302 may change method to GET.

---

### **Q83. Which tool allows mocking of REST APIs for testing?**

* A. Jenkins
* B. Swagger
* C. WireMock ✅
* D. Kubernetes
  ✔ WireMock allows simulating REST endpoints.
  ❌ Jenkins is CI/CD, not API mocker.

---

### **Q84. What’s the typical format of REST API error messages?**

* A. HTML
* B. CSV
* C. JSON with message, code ✅
* D. XML with hash
  ✔ Best practice is structured JSON: `{error, message, code}`
  ❌ HTML is for browsers.

---

### **Q85. Which method retrieves metadata about the resource capabilities?**

* A. HEAD
* B. GET
* C. OPTIONS ✅
* D. TRACE
  ✔ OPTIONS returns allowed HTTP methods.
  ❌ TRACE echoes request.

---

### **Q86. What does 100 Continue mean in HTTP?**

* A. Success
* B. Retry later
* C. Server ready for request body ✅
* D. Request complete
  ✔ Used in two-phase POST for large bodies.
  ❌ Rarely needed manually.

---

### **Q87. Which HTTP status means precondition failed?**

* A. 428
* B. 412 ✅
* C. 409
* D. 401
  ✔ 412 = Failed `If-Match`, `If-Unmodified-Since`, etc.
  ❌ 428 = Precondition Required

---

### **Q88. What’s the best method to update only a specific field?**

* A. PUT
* B. PATCH ✅
* C. POST
* D. HEAD
  ✔ PATCH updates partial fields.
  ❌ PUT replaces the whole resource.

---

### **Q89. Which status code represents Too Early in HTTP/2?**

* A. 425 ✅
* B. 429
* C. 404
* D. 415
  ✔ 425 = Too Early (to retry in early TLS).
  ❌ Very rare.

---

### **Q90. What’s the best way to version a breaking REST change?**

* A. Add query param
* B. Change header
* C. Change URI path (e.g., /v2) ✅
* D. Modify method
  ✔ URI versioning is most transparent and widely used.

---

### **Q91. What is the purpose of `Link` header in pagination?**

* A. Return JWT
* B. Caching
* C. Indicate next/prev page ✅
* D. Retry-After
  ✔ Used to communicate navigation in paginated APIs.

---

### **Q92. What should the DELETE method return if the resource doesn't exist?**

* A. 404 ✅
* B. 200
* C. 204
* D. 500
  ✔ DELETE on missing resource = 404
  ❌ 204 is used for successful deletion.

---

### **Q93. Which response header helps detect stale content?**

* A. Authorization
* B. Cache-Control
* C. ETag ✅
* D. Referer
  ✔ ETag is used to validate cached resources.

---

### **Q94. In REST, which characteristic does statelessness enforce?**

* A. High availability
* B. Server stores no client state ✅
* C. Token reuse
* D. Client remembers cookies
  ✔ Server processes each request in isolation.

---

### **Q95. What’s the best practice for DELETE success with no content?**

* A. 404
* B. 200
* C. 204 ✅
* D. 403
  ✔ 204 = success, no content
  ❌ 200 implies content.

---

### **Q96. What should REST responses be?**

* A. Human-readable
* B. Machine-readable ✅
* C. Binary
* D. ASCII
  ✔ JSON/XML for machines to consume.

---

### **Q97. What is the purpose of rate limiting headers (e.g., X-RateLimit-Remaining)?**

* A. Inform client about auth
* B. Indicate time zones
* C. Show quota remaining ✅
* D. Encrypt token
  ✔ These help APIs enforce fair use.

---

### **Q98. What is the correct status for successful resource creation using POST?**

* A. 200
* B. 201 ✅
* C. 202
* D. 204
  ✔ 201 = created
  ❌ 204 = no content

---

### **Q99. Which header lets you specify languages in REST?**

* A. Content-Type
* B. Accept-Encoding
* C. Accept-Language ✅
* D. Referer
  ✔ Accept-Language negotiates response localization.

---

### **Q100. What happens if a PATCH request is malformed?**

* A. 304
* B. 400 ✅
* C. 403
* D. 204
  ✔ Malformed JSON or field = 400 Bad Request

---

✅ That completes **REST Questions 81–100**.
Shall I continue with **REST MCQs 101–150**?
Continuing with ✅ **Advanced REST API MCQs (101–150)**

---

### **Q101. Which of the following is a valid REST URI for a specific user with ID 42?**

* A. `/user/42`
* B. `/users?id=42`
* C. `/users/42` ✅
* D. `/users?id==42`
  ✔ `/users/42` is RESTful — it identifies the resource directly.
  ❌ Query strings are more typical for filtering, not identification.

---

### **Q102. Which protocol-level cache strategy uses `If-None-Match`?**

* A. Cookie cache
* B. Cache-Control
* C. ETag validation ✅
* D. Session-based caching
  ✔ `If-None-Match` validates ETag for cache freshness.
  ❌ It’s not for setting expiry.

---

### **Q103. Which HTTP status code means the request is syntactically correct but cannot be processed semantically?**

* A. 400
* B. 422 ✅
* C. 409
* D. 403
  ✔ 422 = Unprocessable Entity
  ❌ 400 = Syntax error; 409 = Conflict.

---

### **Q104. What status code is appropriate for an expired token?**

* A. 401 ✅
* B. 403
* C. 400
* D. 404
  ✔ 401 = invalid or expired token (unauthorized)
  ❌ 403 = authorized but forbidden

---

### **Q105. Which of these HTTP methods is NOT allowed to have a request body according to spec?**

* A. GET ✅
* B. POST
* C. PUT
* D. PATCH
  ✔ GET must not change state or carry a body
  ❌ Others can use request bodies.

---

### **Q106. What does a `Retry-After` header indicate?**

* A. Server error
* B. How long to wait before retrying ✅
* C. Auth expiration
* D. Token refresh
  ✔ Retry-After is used with 429 or 503
  ❌ It doesn’t auto-refresh tokens.

---

### **Q107. What are resource identifiers in REST typically?**

* A. Session tokens
* B. URLs ✅
* C. IP addresses
* D. Auth headers
  ✔ URLs uniquely identify REST resources
  ❌ Not network or session info.

---

### **Q108. Which content type is preferred for API documentation in OpenAPI?**

* A. application/json ✅
* B. text/html
* C. text/plain
* D. application/javascript
  ✔ JSON is the standard for Swagger/OpenAPI.
  ❌ HTML is for web rendering, not APIs.

---

### **Q109. What status code indicates the client must upgrade protocol?**

* A. 426 ✅
* B. 402
* C. 408
* D. 403
  ✔ 426 = Upgrade Required
  ❌ Rare but used with TLS requirements.

---

### **Q110. Which HTTP method is defined as "safe" and "idempotent"?**

* A. PUT
* B. GET ✅
* C. POST
* D. PATCH
  ✔ GET does not modify state and can be called multiple times safely.

---

### **Q111. What format should REST URIs follow?**

* A. CamelCase
* B. Snake\_case
* C. kebab-case ✅
* D. PascalCase
  ✔ URIs use lowercase and hyphens (e.g., `/user-profile`)
  ❌ Not programming styles.

---

### **Q112. What kind of REST response structure supports HATEOAS?**

* A. Flat
* B. HTML
* C. Hyperlinked JSON ✅
* D. JWT
  ✔ HATEOAS uses links to other actions/resources in the response
  ❌ Not just raw data

---

### **Q113. Which approach is best for filtering data in REST?**

* A. Headers
* B. URI path
* C. Query parameters ✅
* D. Cookies
  ✔ Query parameters like `?status=active`
  ❌ URI path is for identity.

---

### **Q114. What is the most RESTful way to expose related sub-resources?**

* A. /user?orders
* B. /orders/user
* C. /users/1/orders ✅
* D. /orders?user\_id=1
  ✔ Nested paths are intuitive and RESTful.
  ❌ Query params are for filters, not structure.

---

### **Q115. What is the recommended response code for a PUT that creates a resource?**

* A. 200
* B. 201 ✅
* C. 204
* D. 202
  ✔ 201 = Resource created
  ❌ 200 = updated; 204 = no content

---

### **Q116. What header indicates token expiration in JWT-based systems?**

* A. Expires-In ✅
* B. Authorization
* C. Content-Type
* D. Cache-Control
  ✔ Often custom `Expires-In` or in the JWT payload
  ❌ Not standard HTTP header

---

### **Q117. What is REST API “discoverability”?**

* A. URL shortening
* B. Link relations between resources ✅
* C. OAuth login
* D. Swagger docs
  ✔ HATEOAS enables discoverability
  ❌ Docs ≠ discoverability

---

### **Q118. Which HTTP verb is not idempotent?**

* A. PUT
* B. DELETE
* C. PATCH
* D. POST ✅
  ✔ POST = may create new resource each time
  ❌ PUT/DELETE = same result every time

---

### **Q119. What is the main benefit of pagination in REST?**

* A. Faster database
* B. Simpler routes
* C. Reduced payload ✅
* D. Auth performance
  ✔ Pagination avoids returning massive datasets

---

### **Q120. What does 505 status code mean?**

* A. Server Error
* B. HTTP Version Not Supported ✅
* C. Request Timeout
* D. Proxy Refused
  ✔ 505 = server does not support requested HTTP version

---

### **Q121. Which method is used for discovering REST capabilities (in OpenAPI)?**

* A. PATCH
* B. GET
* C. OPTIONS ✅
* D. HEAD
  ✔ OPTIONS = lists supported methods, often in docs.

---

### **Q122. What structure does a JSON error payload follow?**

* A. {message, timestamp}
* B. {error, code, details} ✅
* C. \[error, status]
* D. <error> XML
  ✔ Standard: `{ "error": "Invalid ID", "code": 400 }`

---

### **Q123. Which header enables cross-domain REST requests?**

* A. X-Domain
* B. Cross-Origin
* C. Access-Control-Allow-Origin ✅
* D. Referer
  ✔ CORS is handled with `Access-Control-Allow-Origin`

---

### **Q124. What’s a good HTTP response code for a successful PATCH?**

* A. 200 ✅
* B. 204
* C. 201
* D. 400
  ✔ 200 or 204 for successful update
  ❌ 201 = creation

---

### **Q125. What’s the most RESTful way to expose a list of products?**

* A. /getProducts
* B. /products ✅
* C. /product-listing
* D. /productsList
  ✔ REST recommends resource nouns, not verbs

---

### **Q126–150 (Final Batch)** coming next — continue?
Here is the final batch ✅ **Advanced REST API MCQs (126–150)** — each with explanation:

---

### **Q126. What status code is appropriate for an invalid HTTP method on an endpoint?**

* A. 400
* B. 405 ✅
* C. 403
* D. 406
  ✔ 405 = Method Not Allowed
  ❌ 406 = Not Acceptable (used for content negotiation)

---

### **Q127. What is the purpose of `OPTIONS` preflight request in CORS?**

* A. Return ETag
* B. Validate headers and methods ✅
* C. Renew token
* D. Minimize payload
  ✔ Preflight checks if headers/methods are permitted cross-origin
  ❌ Not about tokens

---

### **Q128. What’s the typical response type for a REST API health check endpoint?**

* A. XML
* B. HTML
* C. Plain text or JSON ✅
* D. JavaScript
  ✔ Health endpoints return minimal content — often JSON or plain text

---

### **Q129. What status code is appropriate for a malformed JWT token?**

* A. 200
* B. 401 ✅
* C. 403
* D. 500
  ✔ 401 = Unauthorized
  ❌ 403 = Authenticated but access denied

---

### **Q130. What REST design principle requires uniform interfaces?**

* A. Scalability
* B. Statelessness
* C. REST constraint ✅
* D. Authentication
  ✔ REST constraint: uniform interface (URIs, methods, media types)

---

### **Q131. Which HTTP header is used to compress response bodies?**

* A. Accept-Encoding ✅
* B. Transfer-Encoding
* C. Content-Type
* D. X-Compress
  ✔ `Accept-Encoding: gzip, deflate`
  ❌ Not `X-*` proprietary headers

---

### **Q132. What does the `Vary` header do in HTTP caching?**

* A. Blocks duplicate requests
* B. Prevents ETag reuse
* C. Controls cache key variation ✅
* D. Enables TLS
  ✔ `Vary: Accept-Encoding` makes caches respond differently based on request headers

---

### **Q133. Which is NOT a valid HTTP caching directive?**

* A. no-store
* B. public
* C. max-speed ✅
* D. no-cache
  ✔ `max-speed` is invalid; others are legit cache-control values

---

### **Q134. What should be returned if a requested content type is not supported?**

* A. 400
* B. 403
* C. 406 ✅
* D. 401
  ✔ 406 = Not Acceptable (based on Accept header)

---

### **Q135. Which is a valid REST convention for a collection resource?**

* A. /userList
* B. /getUsers
* C. /users ✅
* D. /fetch-users
  ✔ REST uses nouns (`/users`) not actions

---

### **Q136. What status code means a client sent too many headers?**

* A. 431 ✅
* B. 429
* C. 422
* D. 414
  ✔ 431 = Request Header Fields Too Large

---

### **Q137. How should a REST API support sorting?**

* A. Cookie
* B. HTTP Header
* C. Query Parameter ✅
* D. Subdomain
  ✔ Example: `?sort=name&order=asc`

---

### **Q138. What is the best response to an unsupported media type in request?**

* A. 400
* B. 403
* C. 415 ✅
* D. 301
  ✔ 415 = Unsupported Media Type

---

### **Q139. Which REST response code indicates a locked resource?**

* A. 423 ✅
* B. 403
* C. 408
* D. 412
  ✔ 423 = Locked (WebDAV extension)

---

### **Q140. What is the role of HATEOAS in REST?**

* A. Disable redirects
* B. Limit bandwidth
* C. Add hypermedia links to resources ✅
* D. Token refresh
  ✔ HATEOAS provides navigation within API via links

---

### **Q141. When should 202 Accepted be returned?**

* A. When request failed
* B. When task is being processed async ✅
* C. After deletion
* D. After a GET
  ✔ 202 = Accepted for processing but not yet complete

---

### **Q142. What’s the best practice when returning a list of 0 items?**

* A. 204
* B. 200 with empty array ✅
* C. 404
* D. 403
  ✔ 200 + `[]` is REST-friendly
  ❌ 204 = No content (not ideal for lists)

---

### **Q143. How do you return validation errors in REST?**

* A. 401
* B. 400 ✅
* C. 200
* D. 204
  ✔ 400 = Bad Request for validation issues

---

### **Q144. What is HAL (Hypertext Application Language)?**

* A. Caching system
* B. Hypermedia format for REST APIs ✅
* C. Rate limiter
* D. API versioning system
  ✔ HAL provides link-based JSON structure

---

### **Q145. Which status indicates client request timeout?**

* A. 400
* B. 408 ✅
* C. 504
* D. 429
  ✔ 408 = Client didn’t send request in time

---

### **Q146. Which status code should be returned when a POST request creates multiple resources?**

* A. 200
* B. 201 ✅
* C. 202
* D. 204
  ✔ Still a creation — 201 is valid even for multiple

---

### **Q147. What does 511 status mean?**

* A. Proxy error
* B. Network auth required ✅
* C. Host unreachable
* D. Token expired
  ✔ 511 = Captive portal or network-level auth required

---

### **Q148. What’s a typical error handling format in REST APIs?**

* A. XML + schema
* B. HTML
* C. JSON with code, message ✅
* D. Raw text
  ✔ JSON standard: `{ "error": "Invalid", "code": 400 }`

---

### **Q149. What is `x-request-id` used for?**

* A. Auth token
* B. Cache key
* C. Request tracking and logging ✅
* D. IP validation
  ✔ Helps trace logs across systems

---

### **Q150. Which HTTP spec allows PATCH method?**

* A. RFC 2616
* B. HTTP/0.9
* C. RFC 5789 ✅
* D. RFC 7231
  ✔ PATCH was formally introduced in RFC 5789

---

✅ That's **150 Advanced REST API MCQs** completed.

Would you like the **final 50 questions (151–200)** now?
Here’s the final batch of ✅ **Advanced REST API MCQs (151–200)** — each with detailed explanations:

---

### **Q151. Which status code indicates the request was valid but the response is intentionally blank?**

* A. 204 ✅
* B. 200
* C. 403
* D. 400
  ✔ 204 = No Content, used when the operation succeeded but there's nothing to return
  ❌ 200 = returns content

---

### **Q152. Which design principle is **NOT** part of REST constraints?**

* A. Statelessness
* B. Client-server
* C. Layered system
* D. Session management ✅
  ✔ REST requires statelessness, so session management violates it

---

### **Q153. What’s the proper status for an API that denies access based on user’s role?**

* A. 401
* B. 403 ✅
* C. 200
* D. 202
  ✔ 403 = Authenticated but not authorized

---

### **Q154. Which is a **non-standard** HTTP method?**

* A. GET
* B. POST
* C. FETCH ✅
* D. PATCH
  ✔ FETCH is not part of the HTTP/1.1 or HTTP/2 spec

---

### **Q155. What does 424 Failed Dependency mean?**

* A. The request depends on another that failed ✅
* B. The client’s auth is invalid
* C. The data is invalid
* D. The server is overloaded
  ✔ 424 is part of WebDAV extensions

---

### **Q156. What is the main use of HTTP TRACE?**

* A. Update resource
* B. Debugging request path ✅
* C. Cache control
* D. Modify headers
  ✔ TRACE echoes back request headers

---

### **Q157. In REST, which keyword is **not** standard in headers?**

* A. Content-Type
* B. X-Custom-Trace ✅
* C. Accept
* D. Authorization
  ✔ `X-` headers are non-standard unless documented

---

### **Q158. What is `application/problem+json` used for?**

* A. File upload
* B. Auth
* C. Structured error responses ✅
* D. Token delivery
  ✔ Defined in RFC 7807 for standardized error responses

---

### **Q159. Which status code means “proxy received an invalid response”?**

* A. 500
* B. 502 ✅
* C. 504
* D. 400
  ✔ 502 = Bad Gateway (proxy issue)

---

### **Q160. What does `Accept: */*` in headers mean?**

* A. Accept only JSON
* B. No response allowed
* C. Accept any media type ✅
* D. Accept GZIP
  ✔ `*/*` = wildcard for all content types

---

### **Q161. When is status 504 returned?**

* A. Server overload
* B. Authentication failed
* C. Gateway timeout ✅
* D. Resource conflict
  ✔ 504 = upstream server didn’t respond in time

---

### **Q162. What header is often included in rate-limited APIs?**

* A. Retry-After ✅
* B. Authorization
* C. ETag
* D. Location
  ✔ Retry-After tells when to try again

---

### **Q163. Which is the best REST practice for delete confirmation?**

* A. Return 404
* B. Return 200 with message
* C. Return 204 ✅
* D. Return 201
  ✔ 204 = delete successful, no content

---

### **Q164. What’s the correct status code if the client sent a payload too large?**

* A. 403
* B. 413 ✅
* C. 431
* D. 422
  ✔ 413 = Payload Too Large

---

### **Q165. What’s the role of an API Gateway in REST architecture?**

* A. DB replication
* B. Code compilation
* C. Reverse proxy, rate-limiting, logging ✅
* D. Frontend template rendering
  ✔ API Gateway handles cross-cutting concerns

---

### **Q166. Which content type header represents URL-encoded form data?**

* A. application/json
* B. application/xml
* C. multipart/form-data
* D. application/x-www-form-urlencoded ✅
  ✔ Used for traditional form submissions

---

### **Q167. What does the `Range` header enable?**

* A. Pagination
* B. Partial resource delivery ✅
* C. Sorting
* D. Server push
  ✔ `Range` = byte serving (e.g., streaming video)

---

### **Q168. What is a canonical URL?**

* A. A redirect URL
* B. Official URI for a resource ✅
* C. Session URI
* D. Error log URL
  ✔ Canonical URI = preferred reference point for a resource

---

### **Q169. Which status code implies resource has been permanently deleted?**

* A. 404
* B. 410 ✅
* C. 403
* D. 204
  ✔ 410 = Gone (permanently)

---

### **Q170. What’s the primary benefit of using REST over SOAP?**

* A. Schema enforcement
* B. Stateless, lightweight ✅
* C. Strong typing
* D. WS-Security
  ✔ REST is less verbose and HTTP-native

---

### **Q171. What does status 417 mean?**

* A. Server not found
* B. Request Timeout
* C. Expectation Failed ✅
* D. Invalid header
  ✔ 417 = Expect header requirements failed

---

### **Q172. How are enums typically represented in REST?**

* A. Encrypted
* B. JSON string values ✅
* C. Integers only
* D. Session cookies
  ✔ Use strings like `"status": "active"`

---

### **Q173. What’s the best REST practice for boolean flags in URLs?**

* A. /resource?active=yes ✅
* B. /resource/true
* C. /resource?1
* D. /resource\:active
  ✔ Query parameters for filtering flags

---

### **Q174. What status code means too many concurrent connections?**

* A. 429 ✅
* B. 400
* C. 401
* D. 500
  ✔ 429 = Too Many Requests

---

### **Q175. What is the purpose of OPTIONS preflight in CORS?**

* A. Handle file downloads
* B. Validate endpoint signature
* C. Check if browser can safely make the request ✅
* D. Store session
  ✔ It protects browsers from insecure cross-origin calls

---

### **Q176. What status code signals that authentication is required via a proxy?**

* A. 403
* B. 401
* C. 407 ✅
* D. 426
  ✔ 407 = Proxy Authentication Required

---

### **Q177. When is 428 Precondition Required used?**

* A. Always with PATCH
* B. When `If-Match` or `If-Unmodified-Since` is required ✅
* C. During login
* D. With GET
  ✔ 428 = optimistic concurrency control enforcement

---

### **Q178. Which of these is a REST anti-pattern?**

* A. Use of nouns
* B. Stateless design
* C. Tunneling POST with `_method=PUT` ✅
* D. JSON error responses
  ✔ Tunneling methods breaks REST constraints

---

### **Q179. Which is the correct way to specify multiple values for one filter?**

* A. /items?type=a\&type=b ✅
* B. /items?type=a,b
* C. /items?type=\[a,b]
* D. /items?type{a,b}
  ✔ Repeated query params are standard

---

### **Q180. What is the role of HAL in REST?**

* A. Authorization
* B. Hypermedia linking ✅
* C. Debug logging
* D. Token parsing
  ✔ HAL adds HATEOAS-style hypermedia in JSON

---

### **Q181. When should you use 202 instead of 201?**

* A. When response is JSON
* B. When request is queued or async ✅
* C. When resource is deleted
* D. When auth fails
  ✔ 202 = Accepted for processing later

---

### **Q182. What is the key benefit of self-descriptive messages?**

* A. Lower payload
* B. Language translation
* C. Each request contains all required info ✅
* D. Response encryption
  ✔ REST encourages self-sufficient request structure

---

### **Q183. Which tool provides mock REST APIs?**

* A. Figma
* B. SwaggerHub ✅
* C. Git
* D. Jenkins
  ✔ SwaggerHub can mock and document APIs

---

### **Q184. What is REST versioning via headers called?**

* A. URI versioning
* B. Media type versioning ✅
* C. Semantic versioning
* D. Custom header versioning
  ✔ Uses `Accept: application/vnd.company.v1+json`

---

### **Q185. What is the HTTP status for URI too long?**

* A. 414 ✅
* B. 431
* C. 400
* D. 408
  ✔ 414 = URI Too Long

---

### **Q186. What’s the best practice for soft deletes in REST?**

* A. Use DELETE
* B. Use PATCH to set `is_deleted=true` ✅
* C. Send HEAD
* D. Use 410 Gone
  ✔ PATCH preserves data, flags deletion

---

### **Q187. Which is a valid custom header?**

* A. X-Custom-Trace-ID ✅
* B. Y-Trace
* C. CUSTOM-ID
* D. Data-Log
  ✔ X- prefix is legacy, still acceptable

---

### **Q188. How do you specify multiple Accept types?**

* A. Accept: json,xml
* B. Accept: \[json, xml]
* C. Accept: application/json, application/xml ✅
* D. Accept-Type: dual
  ✔ Comma-separated MIME types are standard

---

### **Q189. What’s a good status code for successful login?**

* A. 200 ✅
* B. 201
* C. 204
* D. 403
  ✔ 200 = OK
  ❌ Login doesn’t create resource

---

### **Q190. What is the correct status for unsupported Accept header?**

* A. 406 ✅
* B. 415
* C. 404
* D. 400
  ✔ 406 = Not Acceptable based on Accept header

---

### **Q191. How should a RESTful API expose file download?**

* A. Use GET with content-disposition header ✅
* B. Use POST
* C. Use PATCH
* D. Use OPTIONS
  ✔ Content-Disposition: attachment; filename="file.txt"

---

### **Q192. What does “idempotent” mean in REST?**

* A. Request changes each time
* B. Request has state
* C. Request has same effect when repeated ✅
* D. Request returns error
  ✔ Idempotency ensures predictable results

---

### **Q193. Which code is for “loop detected”?**

* A. 507
* B. 508 ✅
* C. 510
* D. 400
  ✔ 508 = WebDAV extension for infinite loop prevention

---

### **Q194. What’s the correct MIME type for OpenAPI documents?**

* A. application/swagger+json
* B. application/json
* C. application/vnd.oai.openapi+json ✅
* D. application/yaml
  ✔ Official MIME type per OpenAPI spec

---

### **Q195. What is the purpose of the `Allow` header?**

* A. List valid tokens
* B. List supported HTTP methods ✅
* C. Enable TLS
* D. Indicate content size
  ✔ Used with 405 Method Not Allowed

---

### **Q196. What is 510 Not Extended?**

* A. Resource limit
* B. Server crashed
* C. Further extensions required ✅
* D. Auth expired
  ✔ 510 = extension header required (WebDAV)

---

### **Q197. What’s a good use for OPTIONS in REST?**

* A. Upload
* B. Validation
* C. Return allowed methods ✅
* D. Authorization
  ✔ OPTIONS lists what methods are allowed for a resource

---

### **Q198. What’s a best practice for large REST responses?**

* A. GZIP compression ✅
* B. HTML rendering
* C. Queryless URIs
* D. Raw XML
  ✔ GZIP reduces size significantly

---

### **Q199. What status code means client closed the request before server response?**

* A. 408
* B. 499 ✅ *(Nginx-specific)*
* C. 504
* D. 400
  ✔ 499 = Client Closed Request (Nginx custom)

---

### **Q200. Which HTTP header is used to trace requests across systems?**

* A. Trace-ID ✅
* B. Auth-Token
* C. Cache-Key
* D. ETag
  ✔ Used in distributed tracing systems

---

✅ **All 200 REST API Questions Completed!**

Would you like a summary index of all 200, or should we continue with **GraphQL or FastAPI/SQLAlchemy** next?


