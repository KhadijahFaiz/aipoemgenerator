describe('AI Poem Generator', () => {
    it('loads the app homepage', () => {
      cy.visit('http://localhost:8080')
      cy.contains('AI Poem Generator') // check homepage text
    })
  
    it('navigates to Generate Poem page', () => {
      cy.visit('http://localhost:8080')
  
      // Click the Generate Poem link
      cy.contains('Generate Poem').click()
  
      // Confirm that we are on the Generate Poem page
      cy.url().should('include', '/generate')
      cy.contains('Generate') // heading/button on that page
    })
  })
  
  describe('Poem Genie - Generate Poem', () => {
    beforeEach(() => {
      cy.visit('http://localhost:8080')
      cy.contains('Generate Poem').click()
      cy.url().should('include', '/generate')
    })
  
    it('fills out form and generates a poem', () => {
      // Intercept the API call (wildcard to match localhost or 127.0.0.1)
      cy.intercept('POST', '**/api/generate-poem').as('generatePoem')
  
      // Fill out form
      cy.get('#theme').select('Love')
      cy.get('#style').select('Sonnet')
      cy.get('#emotion').select('Sadness')
  
      // Submit form
      cy.get('button[type="submit"]').click()
  
      // Wait for the backend response (up to 20s)
      cy.wait('@generatePoem', { timeout: 20000 })
  
      // Check Generated Poem section exists
      cy.contains('h3', 'Generated Poem', { timeout: 20000 })
        .should('be.visible')
  
      // Check poem text is not empty
      cy.get('.poem-display pre', { timeout: 50000 })
        .invoke('text')
        .should('not.be.empty')
    })
  
    it('shows alert if theme is not selected', () => {
      cy.get('#style').select('Haiku')
      cy.get('#emotion').select('Joy')
  
      cy.get('button[type="submit"]').click()
  
      cy.on('window:alert', (txt) => {
        expect(txt).to.contains('Please select a theme.')
      })
    })
  })
  