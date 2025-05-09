Here is the complete and expanded **Module 7: Guards & Route Protection** section:

---

## 🔐 Module 7: Guards & Route Protection

### 📚 Concepts and Definitions:

* **Guard**: A service that determines whether a particular route can be accessed or exited.
* **CanActivate**: Prevents access to a route unless certain conditions (like login) are met.
* **CanActivateChild**: Applies route protection to all child routes of a module.
* **CanLoad**: Prevents a lazy-loaded module from loading unless authorized.
* **CanDeactivate**: Stops navigation away from a component if form data is unsaved.
* **Router**: Angular’s service to redirect based on guard logic.
* **ActivatedRouteSnapshot / RouterStateSnapshot**: Represent the state of the route before activation.

---

### 📦 Where It Fits in Angular Architecture:

Guards form the **security and navigation control layer** of your application. They ensure:

* Unauthorized users cannot access private modules
* Users are prompted when navigating away with unsaved data
* Data or roles are verified before rendering critical views

They directly integrate with the router and complement authentication/authorization mechanisms.

---

### 🧠 Best Practices:

* Keep guard logic lean. Delegate complex logic to services like `AuthService` or `PermissionService`.
* Return `Observable<boolean>` if the check involves async operations.
* Combine multiple guards per route if needed (auth + role + feature toggle).
* Avoid using guards for UI state; they’re meant for navigation flow.

---

### 🛠️ Example:

**Auth Guard Example (`auth.guard.ts`)**:

```ts
@Injectable({ providedIn: 'root' })
export class AuthGuard implements CanActivate {
  constructor(private auth: AuthService, private router: Router) {}

  canActivate(): boolean {
    if (!this.auth.isLoggedIn()) {
      this.router.navigate(['/login']);
      return false;
    }
    return true;
  }
}
```

**Route Configuration:**

```ts
const routes: Routes = [
  { path: 'admin', component: AdminComponent, canActivate: [AuthGuard] },
  { path: 'settings', component: SettingsComponent, canDeactivate: [UnsavedChangesGuard] }
];
```

**Unsaved Changes Guard (`can-deactivate.guard.ts`)**:

```ts
export interface CanComponentDeactivate {
  canDeactivate: () => boolean | Observable<boolean>;
}

@Injectable({ providedIn: 'root' })
export class CanDeactivateGuard implements CanDeactivate<CanComponentDeactivate> {
  canDeactivate(component: CanComponentDeactivate): boolean | Observable<boolean> {
    return component.canDeactivate ? component.canDeactivate() : true;
  }
}
```

---

### ❌ Common Pitfalls:

* Using `CanActivate` when `CanLoad` is required for lazy-loaded modules.
* Not handling Observables returned from guard methods (e.g., missing `.pipe(map())`).
* Performing heavy logic in guards (e.g., nested service calls) instead of moving it to services.
* Forgetting to register guards in the route configuration.

---

### 🧩 Bonus Tips:

* Use `Resolve` in tandem with guards to preload data before navigating to the route.
* Chain multiple guards to layer checks (e.g., login, permissions, plan access).
* Guards can also be used to redirect logged-in users from public routes like `/login`.

---

Would you like to proceed with **Module 8: Testing with Jasmine, Karma, and TestBed** next?
