import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { tap } from 'rxjs/operators';

@Injectable({ providedIn: 'root' })
export class AuthService {
  private baseUrl = '/api/auth';
  private _token: string | null = localStorage.getItem('token');

  constructor(private http: HttpClient) {}

  get token(): string | null { return this._token; }
  get isLoggedIn(): boolean { return !!this._token; }

  login(email: string, password: string) {
    return this.http.post<{ token: string }>(`${this.baseUrl}/login`, { email, password })
      .pipe(tap(res => {
        this._token = res.token;
        localStorage.setItem('token', res.token);
      }));
  }

  register(email: string, password: string) {
    return this.http.post(`${this.baseUrl}/register`, { email, password });
  }

  logout() {
    this._token = null;
    localStorage.removeItem('token');
  }
}

