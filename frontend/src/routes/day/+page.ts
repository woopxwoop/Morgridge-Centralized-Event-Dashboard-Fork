import type { PageLoad } from './$types';
import { redirect } from '@sveltejs/kit';
import { isValidIsoDate } from '$lib/utils/date';

export const load: PageLoad = ({ url }) => {
	const selectedDate = url.searchParams.get('date') ?? null;
	const eventParam = url.searchParams.get('event');
	const expandedEventId =
		eventParam !== null && /^\d+$/.test(eventParam) ? Number(eventParam) : null;

	if (selectedDate && !isValidIsoDate(selectedDate)) {
		throw redirect(302, '/');
	}

	return { selectedDate, expandedEventId };
};
