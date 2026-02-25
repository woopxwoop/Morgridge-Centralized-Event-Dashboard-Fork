import type { PageLoad } from './$types';
import { redirect } from '@sveltejs/kit';

function isValidIsoDate(value: string): boolean {
	if (!/^\d{4}-\d{2}-\d{2}$/.test(value)) {
		return false;
	}

	const [yearText, monthText, dayText] = value.split('-');
	const year = Number(yearText);
	const month = Number(monthText);
	const day = Number(dayText);

	// makes sure day is within month and because month is 0 indexed, subtract 1
	const parsedDate = new Date(year, month - 1, day);

	return (
		parsedDate.getFullYear() === year &&
		parsedDate.getMonth() === month - 1 &&
		parsedDate.getDate() === day
	);
}

export const load: PageLoad = ({ url }) => {
	const selectedDate = url.searchParams.get('date') ?? null;

	if (selectedDate && !isValidIsoDate(selectedDate)) {
		throw redirect(302, '/');
	}

	return { selectedDate };
};
