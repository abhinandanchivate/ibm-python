Here is the fully expanded **Module 6: HTTPClient & Interceptors** in the same format as previous modules:

---

## 🌐 Module 6: HTTPClient & Interceptors

### 📚 Concepts and Definitions:

* **HttpClient**: A service that enables communication with backend services over HTTP. It supports GET, POST, PUT, DELETE, etc.
* **HttpClientModule**: Must be imported in the Angular module to enable HTTP features.
* **HttpInterceptor**: A class that implements `HttpInterceptor` and intercepts every outgoing request and incoming response.
* **HttpRequest & HttpResponse**: Represent the request being sent and the response received from the server.
* **HttpHandler**: Passes the request to the next interceptor or backend.
* **pipe(), catchError(), map()**: RxJS operators used to transform and handle request/response data.

### 📦 Where It Fits in Angular Architecture:

This module is part of the **data access and integration layer**. It handles:

* All HTTP-based API communication
* Authentication headers
* Error handling (e.g., token expiration)
* Request/response logging or caching

### 🧠 Best Practices:

* Always create a dedicated service (e.g., `UserService`, `ProductService`) for interacting with a specific backend resource.
* Handle all common headers and tokens via interceptors.
* Use `tap()` or `catchError()` in observables for response logging or transformation.
* Avoid subscribing directly inside services – return the observable to the component instead.

### 🛠️ Example:

**Importing in AppModule:**

```ts
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';

@NgModule({
  imports: [HttpClientModule],
  providers: [
    { provide: HTTP_INTERCEPTORS, useClass: AuthInterceptor, multi: true }
  ]
})
export class AppModule {}
```

**Creating an API Service:**

```ts
@Injectable({ providedIn: 'root' })
export class UserService {
  constructor(private http: HttpClient) {}

  getUsers(): Observable<User[]> {
    return this.http.get<User[]>('/api/users');
  }

  createUser(data: User): Observable<User> {
    return this.http.post<User>('/api/users', data);
  }
}
```

**Basic Interceptor Example:**

```ts
@Injectable()
export class AuthInterceptor implements HttpInterceptor {
  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    const authReq = req.clone({
      headers: req.headers.set('Authorization', 'Bearer token123')
    });
    return next.handle(authReq);
  }
}
```

**Error Handling with catchError:**

```ts
getUsers(): Observable<User[]> {
  return this.http.get<User[]>('/api/users')
    .pipe(catchError(error => {
      console.error('API error:', error);
      return throwError(() => new Error('Something went wrong!'));
    }));
}
```

### ❌ Common Pitfalls:

* Not importing `HttpClientModule` in the root or feature module.
* Manually adding headers for every request instead of using an interceptor.
* Subscribing in services (instead, let the component decide).
* Forgetting to return the `Observable` chain (e.g., missing `return` in interceptor).

### 🧩 Bonus:

* Chain multiple interceptors (logging, auth, error handling).
* Add loading spinners globally via interceptor-based request tracking.
* Integrate retry logic using `retry()` or `retryWhen()` from RxJS.
* Use environment-based API base URLs using `environment.ts`.

---

Would you like to continue with **Module 7: Guards & Route Protection**?
