<script lang="ts">
	import CalendarDayBlock from '$lib/components/CalendarDayBlock.svelte';
	const today = new Date();
	let displayedYear = $state(today.getFullYear());
	let displayedMonth = $state(today.getMonth());

	const firstDayOfMonth = $derived(new Date(displayedYear, displayedMonth, 1));
	const firstDayOfWeek = $derived(firstDayOfMonth.getDay());
	const firstVisibleDate = $derived(new Date(displayedYear, displayedMonth, 1 - firstDayOfWeek));

	const monthLabel = $derived(
		new Intl.DateTimeFormat('en-US', { month: 'long', year: 'numeric' }).format(
			new Date(displayedYear, displayedMonth, 1)
		)
	);

	const days: string[] = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];

	const calendarDays = $derived(
		Array.from({ length: 42 }, (_, index) => {
			const date = new Date(firstVisibleDate);
			date.setDate(firstVisibleDate.getDate() + index);

			return {
				date,
				dayNumber: date.getDate(),
				isCurrentMonth: date.getMonth() === displayedMonth
			};
		})
	);

	const weeks = $derived(
		Array.from({ length: 6 }, (_, weekIndex) =>
			calendarDays.slice(weekIndex * 7, (weekIndex + 1) * 7)
		)
	);

	function shiftMonth(delta: number) {
		const nextMonthDate = new Date(displayedYear, displayedMonth + delta, 1);
		displayedYear = nextMonthDate.getFullYear();
		displayedMonth = nextMonthDate.getMonth();
	}
</script>

<div class="h-full">
	<div class="mb-3 flex items-center justify-between">
		<button type="button" class="rounded border px-3 py-1" onclick={() => shiftMonth(-1)}
			>Prev</button
		>
		<h2 class="text-lg font-semibold">{monthLabel}</h2>
		<button type="button" class="rounded border px-3 py-1" onclick={() => shiftMonth(1)}
			>Next</button
		>
	</div>

	<table class="h-[80%] w-full table-fixed border-collapse">
		<thead class="text-center">
			<tr>
				{#each days as day}
					<th class="p font-medium">{day}</th>
				{/each}
			</tr>
		</thead>
		<tbody class="h-full grid-rows-6">
			{#each weeks as week}
				<tr class="row-span-1">
					{#each week as day}
						<td class="p border align-top">
							<div class={day.isCurrentMonth ? '' : 'opacity-40'}>
								<CalendarDayBlock date={day.date} dayNumber={day.dayNumber} />
							</div>
						</td>
					{/each}
				</tr>
			{/each}
		</tbody>
	</table>
</div>
