import type { EventInfo } from '$lib/mockEvents';
import { parseIsoDate } from '$lib/utils/date';

export function parseEventDate(eventDay: string): Date {
	const [month, day, year] = eventDay.split('/').map(Number);
	return new Date(year, month - 1, day);
}

export function parseEventDateTime(event: Pick<EventInfo, 'eventDay' | 'eventStartTime'>): Date {
	const eventDate = parseEventDate(event.eventDay);
	const [timeValue, meridiem] = event.eventStartTime.split(' ');
	const [hourValue, minuteValue] = timeValue.split(':').map(Number);
	const hours = (hourValue % 12) + (meridiem === 'PM' ? 12 : 0);

	return new Date(
		eventDate.getFullYear(),
		eventDate.getMonth(),
		eventDate.getDate(),
		hours,
		minuteValue,
		0,
		0
	);
}

export function sortEventsChronologically<T extends Pick<EventInfo, 'eventDay' | 'eventStartTime'>>(
	events: T[]
): T[] {
	return [...events].sort(
		(firstEvent, secondEvent) =>
			parseEventDateTime(firstEvent).getTime() - parseEventDateTime(secondEvent).getTime()
	);
}

export function filterEventsByIsoDate<T extends Pick<EventInfo, 'eventDay'>>(
	events: T[],
	selectedDate: string | null
): T[] {
	if (!selectedDate) {
		return [];
	}

	const selectedTime = parseIsoDate(selectedDate).getTime();
	return events.filter((event) => parseEventDate(event.eventDay).getTime() === selectedTime);
}

export function filterEventsBySearchQuery<T extends EventInfo>(events: T[], query: string): T[] {
	const normalizedQuery = query.trim().toLowerCase();

	if (!normalizedQuery) {
		return events;
	}

	return events.filter((event) =>
		[
			event.eventTitle,
			event.eventHost,
			event.eventLocation,
			event.eventDescription,
			event.eventDay
		]
			.join(' ')
			.toLowerCase()
			.includes(normalizedQuery)
	);
}

export function countEventsOnIsoDate<T extends Pick<EventInfo, 'eventDay'>>(
	events: T[],
	selectedDate: string
): number {
	return filterEventsByIsoDate(events, selectedDate).length;
}