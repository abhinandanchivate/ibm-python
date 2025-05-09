Here is the complete and expanded **Module 4: Services & Dependency Injection** section:

---

## 🚀 Module 4: Services & Dependency Injection

### 📚 Concepts and Definitions:

* **Service**:
  A plain TypeScript class annotated with `@Injectable()` that contains business logic, API calls, shared state, or helper functions. Services promote separation of concerns and code reuse.

* **Dependency Injection (DI)**:
  Angular’s built-in design pattern for providing class instances (services) where they are needed, without manually instantiating them. It allows your code to be loosely coupled and easier to test.

* **@Injectable()**:
  A decorator that marks a class as eligible for injection via Angular's injector.

* **Injector Tree**:
  Angular uses a hierarchical tree of injectors. Services provided in the root injector are singleton and shared app-wide.

* **@Inject()**:
  Injects a dependency using an injection token (for interfaces or configuration objects).

* **@Optional(), @Self(), @SkipSelf()**:
  Advanced injection options for controlling resolution scope and fallback logic.

* **providedIn: 'root'**:
  Angular’s tree-shakable way of registering services globally in the root injector.

---

### 📦 Where It Fits in Angular Architecture:

Services and DI are the **business logic and data access layer** of an Angular application. They:

* Power your components without bloating them
* Centralize common logic (auth, logging, transformation, persistence)
* Enable mockability in unit tests
* Integrate APIs with Angular’s reactive change detection model

---

### 🧠 Best Practices:

* Keep services stateless unless sharing data is required.
* Inject services into **constructor**, not by method call.
* Use `providedIn: 'root'` unless module-specific instances are needed.
* Centralize HTTP logic in services, not components.
* Create domain-specific services (AuthService, UserService, etc.)

---

### 🛠️ Example:

**Generating a service:**

```bash
ng generate service services/user
```

**UserService (API handler):**

```ts
@Injectable({ providedIn: 'root' })
export class UserService {
  constructor(private http: HttpClient) {}

  getUserList(): Observable<User[]> {
    return this.http.get<User[]>('/api/users');
  }

  getUserById(id: number): Observable<User> {
    return this.http.get<User>(`/api/users/${id}`);
  }
}
```

**Using it in a component:**

```ts
@Component({ ... })
export class UserListComponent implements OnInit {
  users: User[] = [];

  constructor(private userService: UserService) {}

  ngOnInit(): void {
    this.userService.getUserList().subscribe(users => this.users = users);
  }
}
```

---

### ❌ Common Pitfalls:

* Using the same service instance in root and child modules when they should be isolated.
* Injecting services directly into templates (Angular does not support this).
* Doing too much in a service – separate concerns (e.g., API calls vs. UI state).
* Forgetting to unsubscribe from Observables if the service emits multiple values (unless using `HttpClient`, which completes automatically).

---

### 🧩 Bonus Tips:

* Combine services with `BehaviorSubject` or `ReplaySubject` for shared state.
* Use `InjectionToken` to provide configuration objects.
* Write unit tests for services by mocking HTTP and using spies.
* Avoid calling services inside constructors; use `ngOnInit` instead.

---

Would you like me to continue with **Module 5: Reactive Forms** next in the same style?
