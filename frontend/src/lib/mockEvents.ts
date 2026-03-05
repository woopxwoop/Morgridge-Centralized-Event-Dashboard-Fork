export interface EventInfo {
    id: number;
    eventTitle: string;
    eventHost: string;
    eventLocation: string;
    eventDay: string;
    eventStartTime: string;
    eventDuration: string;
    eventDescription: string;
    food: boolean;
    media: string[];
}

export const mockEvents: EventInfo[] = [
    {
        id: 1,
        eventTitle: 'WebTalks',
        eventHost: 'Weblabs',
        eventLocation: 'Morgridge Hall Rm. 2556',
        eventDay: '3/5/2026',
        eventStartTime: '6 PM',
        eventDuration: '1 hour',
        eventDescription: 'WebLabs is hosting a workshop with a frontend engineer from Fetch on publishing a website using SvelteKit and GitHub Actions. Whether you\'re a frontend warrior or just interested in standing up a portfolio site for your resume, this workshop will have something for everyone! Like usual for WebLabs, this event will feature pizza 🍕',
        food: true,
        media: ["https://i.redd.it/2nj600aenfnf1.png"],
    },
    {
        id: 2,
        eventTitle: 'Craft Night Social',
        eventHost: 'Girls Who Code-Madison Chapter',
        eventLocation: 'Morgridge Hall Student Org Lounge (2nd floor)',
        eventDay: '3/5/2026',
        eventStartTime: '7:30 PM',
        eventDuration: '1 hour',
        eventDescription: 'Join us for a break from studying to decorate our club locker and meet other fellow members! We will have pizza 🍕 and arts/craft supplies 🖌️✂️ for you to make decorations. We hope to see you there!!',
        food: false,
        media: ["https://www.mamp.one/wp-content/uploads/2024/09/image-resources2.jpg"],
    },
    {
        id: 3,
        eventTitle: 'UPL Research Talk',
        eventHost: 'UPL',
        eventLocation: 'Morgridge Hall Rm. 1524',
        eventDay: '3/6/2026',
        eventStartTime: '6:00 PM',
        eventDuration: '1 hour',
        eventDescription: 'The UPL is hosting a talk on getting into research as an undergrad for the first time! I\'ll be sharing what I\'ve personally learned about reaching out to labs, finding advisors, and making the most of your time once you\'re in. Whether you\'re interested in research for grad school, industry, or pure curiosity, feel free to stop by.',
        food: true,
        media: ["https://cdn.discordapp.com/attachments/1423716763711045705/1473462011881848842/flyer.jpg?ex=69a180af&is=69a02f2f&hm=48183abc7d49de6070f133fa6ca6c1f18490fe424c85be3624f3b840ae8c2347&"],
    },
    {
        id: 4,
        eventTitle: 'WebTalks',
        eventHost: 'Weblabs',
        eventLocation: 'Morgridge Hall Rm. 2556',
        eventDay: '3/5/2026',
        eventStartTime: '6 PM',
        eventDuration: '1 hour',
        eventDescription: 'WebLabs is hosting a workshop with a frontend engineer from Fetch on publishing a website using SvelteKit and GitHub Actions. Whether you\'re a frontend warrior or just interested in standing up a portfolio site for your resume, this workshop will have something for everyone! Like usual for WebLabs, this event will feature pizza 🍕',
        food: true,
        media: ["https://i.redd.it/2nj600aenfnf1.png"],
    },
    {
        id: 5,
        eventTitle: 'Craft Night Social',
        eventHost: 'Girls Who Code-Madison Chapter',
        eventLocation: 'Morgridge Hall Student Org Lounge (2nd floor)',
        eventDay: '3/5/2026',
        eventStartTime: '7:30 PM',
        eventDuration: '1 hour',
        eventDescription: 'Join us for a break from studying to decorate our club locker and meet other fellow members! We will have pizza 🍕 and arts/craft supplies 🖌️✂️ for you to make decorations. We hope to see you there!!',
        food: false,
        media: ["https://www.mamp.one/wp-content/uploads/2024/09/image-resources2.jpg"],
    },
    {
        id: 6,
        eventTitle: 'UPL Research Talk',
        eventHost: 'UPL',
        eventLocation: 'Morgridge Hall Rm. 1524',
        eventDay: '3/6/2026',
        eventStartTime: '6:00 PM',
        eventDuration: '1 hour',
        eventDescription: 'The UPL is hosting a talk on getting into research as an undergrad for the first time! I\'ll be sharing what I\'ve personally learned about reaching out to labs, finding advisors, and making the most of your time once you\'re in. Whether you\'re interested in research for grad school, industry, or pure curiosity, feel free to stop by.',
        food: true,
        media: ["https://cdn.discordapp.com/attachments/1423716763711045705/1473462011881848842/flyer.jpg?ex=69a180af&is=69a02f2f&hm=48183abc7d49de6070f133fa6ca6c1f18490fe424c85be3624f3b840ae8c2347&"],
    },
    {
        id: 7,
        eventTitle: 'WebTalks',
        eventHost: 'Weblabs',
        eventLocation: 'Morgridge Hall Rm. 2556',
        eventDay: '3/5/2026',
        eventStartTime: '6 PM',
        eventDuration: '1 hour',
        eventDescription: 'WebLabs is hosting a workshop with a frontend engineer from Fetch on publishing a website using SvelteKit and GitHub Actions. Whether you\'re a frontend warrior or just interested in standing up a portfolio site for your resume, this workshop will have something for everyone! Like usual for WebLabs, this event will feature pizza 🍕',
        food: true,
        media: ["https://i.redd.it/2nj600aenfnf1.png"],
    },
    {
        id: 8,
        eventTitle: 'Craft Night Social',
        eventHost: 'Girls Who Code-Madison Chapter',
        eventLocation: 'Morgridge Hall Student Org Lounge (2nd floor)',
        eventDay: '3/5/2026',
        eventStartTime: '7:30 PM',
        eventDuration: '1 hour',
        eventDescription: 'Join us for a break from studying to decorate our club locker and meet other fellow members! We will have pizza 🍕 and arts/craft supplies 🖌️✂️ for you to make decorations. We hope to see you there!!',
        food: false,
        media: ["https://www.mamp.one/wp-content/uploads/2024/09/image-resources2.jpg"],
    },
    {
        id: 9,
        eventTitle: 'UPL Research Talk',
        eventHost: 'UPL',
        eventLocation: 'Morgridge Hall Rm. 1524',
        eventDay: '3/6/2026',
        eventStartTime: '6:00 PM',
        eventDuration: '1 hour',
        eventDescription: 'The UPL is hosting a talk on getting into research as an undergrad for the first time! I\'ll be sharing what I\'ve personally learned about reaching out to labs, finding advisors, and making the most of your time once you\'re in. Whether you\'re interested in research for grad school, industry, or pure curiosity, feel free to stop by.',
        food: true,
        media: ["https://cdn.discordapp.com/attachments/1423716763711045705/1473462011881848842/flyer.jpg?ex=69a180af&is=69a02f2f&hm=48183abc7d49de6070f133fa6ca6c1f18490fe424c85be3624f3b840ae8c2347&"],
    }
]