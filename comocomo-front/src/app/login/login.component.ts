import { Component } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';

import { UsersApiService } from '../data-model/users/users-api.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.less']
})
export class LoginComponent {

  public loginForm = this.fb.group({
    username: ['', Validators.required],
    password: ['', Validators.required]
  });

  constructor(
    private fb: FormBuilder,
    private router: Router,
    private usersApiService: UsersApiService
  ) { }

  get username() {
    return this.loginForm.get('username');
  }

  get password() {
    return this.loginForm.get('password');
  }

  public onSubmit() {
    const value = this.loginForm.value;
    this.usersApiService.login(value.username, value.password).subscribe(
      () => this.router.navigate(['/day'])
    );
  }

}
