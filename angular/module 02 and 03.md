

---

## 🔬 Module 2: Components & Template Syntax

### 📚 Concepts and Definitions:

* **Component**: A building block of Angular apps, defined using `@Component`, combining logic, template, and styles.
* **Template**: The HTML structure where data is rendered and user events are captured.
* **Data Binding**:

  * **Interpolation**: `{{ value }}` – binds component variables to the template.
  * **Property Binding**: `[property]="value"` – sets DOM properties from component logic.
  * **Event Binding**: `(event)="handler()"` – responds to DOM events in the component class.
  * **Two-Way Binding**: `[(ngModel)]="value"` – syncs user input and class variables.
* **Directives**:

  * **Structural Directives**: Modify DOM layout – `*ngIf`, `*ngFor`, `*ngSwitch`.
  * **Attribute Directives**: Modify appearance – `ngClass`, `ngStyle`, or custom directives.
* **View Encapsulation**: Defines how styles are scoped – `Emulated`, `None`, `ShadowDom`.
* **Change Detection**: Angular's system to keep the DOM in sync with data – `Default` and `OnPush` strategies.
* **Template Reference Variables**: Declared with `#varName`, used to reference DOM or Angular elements.

### 📦 Where It Fits in Angular Architecture:

Components form the **presentation layer**. Every UI element is rendered through a component, and component trees are managed via Angular modules. Template bindings and directives make dynamic rendering possible.

### 🧠 Best Practices:

* Keep components small and focused on a single responsibility.
* Use `OnPush` strategy for performance when data is immutable.
* Use `ng-container` when you need structural directives without adding extra elements.
* Separate layout logic into child components and reuse them.

### 🛠️ Example:

**Component Class:**

```ts
@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.scss']
})
export class UserProfileComponent {
  @Input() user!: User;
  @Output() logout = new EventEmitter<void>();
  toggle = false;
}
```

**Template:**

```html
<div class="card">
  <h2>{{ user.name }}</h2>
  <p>Email: {{ user.email }}</p>
  <button (click)="logout.emit()">Logout</button>
  <div *ngIf="toggle">Details are visible</div>
</div>
```

### ❌ Common Pitfalls:

* Using too much logic in templates – move it to the component class.
* Not encapsulating reusable UI parts into standalone components.
* Forgetting to declare components in the appropriate module.

### 🧩 Bonus:

To make the most out of template syntax:

* Use `ng-content` for content projection
* Use `@ViewChild` to access template reference variables programmatically
* Combine `ngSwitch` with enums for clean conditional rendering

---

## 🔄 Module 3: Routing & Navigation

### 📚 Concepts and Definitions:

* **RouterModule**: Angular module that enables navigation and routing capabilities within the app.
* **AppRoutingModule**: A dedicated module used to centralize and configure all the routes.
* **Routes Array**: Defines the mapping of paths to components using Angular's `Routes` type.
* **RouterOutlet**: A placeholder directive in a component template that renders the component for the active route.
* **RouterLink**: Directive to navigate between routes declaratively in the template.
* **ActivatedRoute**: Service to access route-specific information such as route parameters, query parameters, etc.

### 📦 Where It Fits in Angular Architecture:

Routing is part of the **application shell and navigation layer**. It determines how users interact with and move across different parts of your application and supports module lazy loading, route guards, and URL-based logic.

### 🧠 Best Practices:

* Define all top-level routes in `AppRoutingModule`.
* Use lazy loading for feature modules to improve performance.
* Keep route definitions clean by using feature-level `RoutingModule`s.
* Apply guards to protect routes that require authentication or roles.

### 🛠️ Example:

**Route Configuration:**

```ts
const routes: Routes = [
  { path: '', redirectTo: 'home', pathMatch: 'full' },
  { path: 'home', component: HomeComponent },
  { path: 'users/:id', component: UserProfileComponent },
  { path: 'admin', loadChildren: () => import('./features/admin/admin.module').then(m => m.AdminModule) },
  { path: '**', component: NotFoundComponent }
];
```

**AppRoutingModule:**

```ts
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
```

**Template Usage:**

```html
<a routerLink="/home">Home</a>
<router-outlet></router-outlet>
```

### ❌ Common Pitfalls:

* Forgetting to import `AppRoutingModule` in `AppModule`.
* Not using `pathMatch: 'full'` for default routes.
* Using eager-loaded modules unnecessarily, leading to large bundle sizes.
* Hardcoding route parameters instead of using `ActivatedRoute`.

### 🧩 Bonus:

* Use `Router.navigate()` for programmatic routing.
* Combine `RouterLinkActive` for active state navigation styling.
* Use `Resolve` interface for pre-fetching route data.
* Implement `CanDeactivate` guard for unsaved form protection.

---
