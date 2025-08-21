import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({ providedIn: 'root' })
export class BookingService {
  private baseUrl = '/api/bookings';
  constructor(private http: HttpClient) {}

  create(tripId: string, guests = 1) { return this.http.post(this.baseUrl, { tripId, guests }); }
  mine() { return this.http.get(`${this.baseUrl}/me`); }
  cancel(id: string) { return this.http.delete(`${this.baseUrl}/${id}`); }
}

