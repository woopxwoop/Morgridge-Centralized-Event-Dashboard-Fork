import { derived } from 'svelte/store';
import { mockEvents } from '$lib/mockEvents';
import { filterEventsBySearchQuery, sortEventsChronologically } from '$lib/features/events/utils';
import { calendarSearchQuery } from '$lib/stores/calendar-ui';

const allEvents = sortEventsChronologically(mockEvents);

export const filteredEvents = derived(calendarSearchQuery, ($calendarSearchQuery) =>
	filterEventsBySearchQuery(allEvents, $calendarSearchQuery)
);
