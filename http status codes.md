 **commonly used generic HTTP status codes** categorized by type, along with their meanings:

---

### ✅ **1xx – Informational**
| Code | Meaning                            | Use Case                                      |
|------|------------------------------------|-----------------------------------------------|
| 100  | Continue                           | Interim response; client can continue request |
| 101  | Switching Protocols                | Server switching protocols (e.g., HTTP to WebSocket) |

---

### 🟢 **2xx – Success**
| Code | Meaning                            | Use Case                                      |
|------|------------------------------------|-----------------------------------------------|
| 200  | OK                                 | Request succeeded                             |
| 201  | Created                            | Resource created (e.g., POST)                 |
| 202  | Accepted                           | Request accepted, processing later            |
| 204  | No Content                         | Success, but no content to return             |

---

### 🟡 **3xx – Redirection**
| Code | Meaning                            | Use Case                                      |
|------|------------------------------------|-----------------------------------------------|
| 301  | Moved Permanently                  | Resource permanently moved                    |
| 302  | Found                              | Temporary redirection                         |
| 304  | Not Modified                       | Client can use cached version                 |

---

### 🔴 **4xx – Client Errors**
| Code | Meaning                            | Use Case                                      |
|------|------------------------------------|-----------------------------------------------|
| 400  | Bad Request                        | Malformed syntax or invalid input             |
| 401  | Unauthorized                       | Authentication required                       |
| 403  | Forbidden                          | Authenticated but not allowed                 |
| 404  | Not Found                          | Resource not found                            |
| 405  | Method Not Allowed                 | HTTP method not allowed on resource           |
| 409  | Conflict                           | Conflict in request (e.g., duplicate data)    |
| 422  | Unprocessable Entity               | Validation errors                             |

---

### 🔴 **5xx – Server Errors**
| Code | Meaning                            | Use Case                                      |
|------|------------------------------------|-----------------------------------------------|
| 500  | Internal Server Error              | Generic server error                          |
| 501  | Not Implemented                    | Server doesn't support requested functionality|
| 502  | Bad Gateway                        | Invalid response from upstream server         |
| 503  | Service Unavailable                | Server is temporarily down or overloaded      |
| 504  | Gateway Timeout                    | Timeout from upstream server                  |

---
