class CreateUsersTickets < ActiveRecord::Migration
  def up
    create_table :users_tickets, :id => false do |t|
      t.integer :user_id
      t.integer :ticket_id
    end

    add_index :users_tickets, [:user_id, :ticket_id]
  end

  def down
    drop_table :users_tickets
  end
end
