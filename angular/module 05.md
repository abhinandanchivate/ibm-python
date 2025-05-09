

## 🧾 Module 5: Reactive Forms

### 📚 Concepts and Definitions:

* **ReactiveFormsModule**: A module that provides a model-driven approach to handling form inputs and validations.
* **FormControl**: Tracks the value and status of an individual form input.
* **FormGroup**: A collection of FormControls that track the overall form state.
* **FormBuilder**: A syntactic shortcut for creating instances of FormGroup and FormControl.
* **Validators**: Functions used to validate form inputs (e.g., required, minLength, pattern).
* **valueChanges**: An Observable that emits changes to the value of the form control or group.
* **statusChanges**: Emits the form's validity status (VALID, INVALID, PENDING, DISABLED).

### 📦 Where It Fits in Angular Architecture:

Reactive Forms are part of the **presentation layer**. They provide a flexible and scalable way to build and manage complex forms in Angular applications, especially when forms are dynamic or require extensive validation.

### 🧠 Best Practices:

* Always define forms in the component class for full control and unit testability.
* Group logically related controls together using `FormGroup`.
* Use custom validators for business rules like password match, conditional fields, etc.
* Manage validation messages using reusable functions or dedicated validation services.

### 🛠️ Example:

**Form Initialization:**

```ts
this.registrationForm = this.fb.group({
  fullName: ['', [Validators.required, Validators.minLength(3)]],
  email: ['', [Validators.required, Validators.email]],
  password: ['', [Validators.required, Validators.minLength(6)]],
  confirmPassword: ['']
}, { validators: this.passwordMatch });
```

**Custom Validator:**

```ts
passwordMatch(group: AbstractControl): ValidationErrors | null {
  const pass = group.get('password')?.value;
  const confirm = group.get('confirmPassword')?.value;
  return pass === confirm ? null : { notMatching: true };
}
```

**HTML Template:**

```html
<form [formGroup]="registrationForm" (ngSubmit)="submit()">
  <input formControlName="email" placeholder="Email" />
  <div *ngIf="registrationForm.get('email')?.invalid">Invalid email</div>
</form>
```

### ❌ Common Pitfalls:

* Not importing `ReactiveFormsModule` in the module using the form.
* Accessing `.value` directly in the template instead of using form bindings.
* Submitting a form without checking `form.valid`.
* Nesting controls without properly referencing them in the template.

### 🧩 Bonus:

* Use `FormArray` for forms with dynamic repeating fields.
* Use `patchValue()` to update part of the form.
* Use `form.reset()` to clear the form state.
* Combine `valueChanges` with RxJS operators (e.g., debounceTime) to optimize UX.

---
