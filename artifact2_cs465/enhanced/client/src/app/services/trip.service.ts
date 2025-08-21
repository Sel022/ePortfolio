import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';

@Injectable({ providedIn: 'root' })
export class TripService {
  private baseUrl = '/api/trips';

  constructor(private http: HttpClient) {}

  list(page = 1, limit = 10) {
    const params = new HttpParams().set('page', page).set('limit', limit);
    return this.http.get<{ items: any[], page: number, pages: number, total: number }>(this.baseUrl, { params });
  }

  create(trip: any) { return this.http.post(this.baseUrl, trip); }
  update(id: string, trip: any) { return this.http.put(`${this.baseUrl}/${id}`, trip); }
  remove(id: string) { return this.http.delete(`${this.baseUrl}/${id}`); }
}

